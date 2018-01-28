#!/usr/bin/python3

import time
import random

class ShuangSeQiu:
    def __init__(self, order = None):
        self.__r = random.SystemRandom()
        if not order:
            self.__order = 1
        else:
            self.__order = order
    def randint(self, min, max):
        start = time.time()
        global curr
        global r
        curr = start
        length = max - min + 1
        r = self.__r.getrandbits(8) % length
        while curr < start + self.__order:
            curr = time.time()
            r += self.__r.getrandbits(8)
            r %= length
        return r
    def randRed(self):
        return self.randint(1, 32)
    def randBlue(self):
        return self.randint(1, 16)
    def cast(self):
        red = set()
        while len(red) < 6:
            red.add(self.randRed())
        blue = self.randBlue()
        return (sorted(red), blue)
            
if __name__ == "__main__":
    a = ShuangSeQiu(300)
    for i in range(2):
        print(a.cast())
