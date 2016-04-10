#!/usr/bin/python3

import random

__all__ = ['Random']

class Random(random.Random):
    """Random number generator use /dev/random."""
    def __init__(self):
        self.__fd = open('/dev/random', 'rb')
    def random(self):
        return self.getrandbits(64) / ((1 << 64) - 1)
    def seed(self, s):
        pass
    def getstate(self):
        pass
    def setstate(self, state):
        pass
    def _getrandbits_lt8(self, k):
        ret = 0
        k &= 0x7
        if k == 0:
            return ret
        ret = list(self.__fd.read(1))[0]
        ret &= (1 << k) - 1
        return ret
    def getrandbits(self, k):
        ret = self._getrandbits_lt8(k)
        if k < 8:
            return ret
        data = list(self.__fd.read(k>>3))
        for v in data:
            ret <<= 8
            ret += v
        return ret

    def __exit__(self):
        self.close()
