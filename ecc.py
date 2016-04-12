#!/usr/bin/python3

import prime
import logging

"""Test ECC curve in ECC cryption algorithm."""

class Point:
    def __init__(self, x = 0, y= 0):
        self.__x = x
        self.__y = y
    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, value):
        self.__x = value
    @x.deleter
    def x(self):
        pass
    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self, value):
        self.__y = value
    @y.deleter
    def y(self):
        pass
    def __str__(self):
        return ''.join(['(', str(self.__x), ',', str(self.__y), ')'])

class ZeroPoint(Point):
    def __init__(self):
        pass
    @property
    def x(self):
        pass
    @x.setter
    def x(self, value):
        pass
    @x.deleter
    def x(self):
        pass
    @property
    def y(self):
        pass
    @y.setter
    def y(self, value):
        pass
    @y.deleter
    def y(self):
        pass
    def __str__(self):
        return 'ZeroPoint'

class ECC:
    """Elliptic curve is y^2 = x^3 - ax - b (mod p)."""
    def __init__(self, a = 27397, b = 92791, p = 697967):
        self._a = a
        self._b = b
        self._p = p
        self._logger = logging.getLogger('test.ecc')
        self._logger.debug('a = {0} b = {1} p = {2}'.format(a, b, p))
        self._G = None
    @property
    def G(self):
        if not self._G:
            return self.basePoint()
        else:
            return self._G
    @G.setter
    def G(self, value):
        pass
    @G.deleter
    def G(self):
        pass
    def add(self, p, q):
        r = Point()
        if isinstance(p, ZeroPoint):
            r = q
        elif isinstance(q, ZeroPoint):
            r = p
        elif p.x != q.x:
            s = (p.y - q.y) * prime.invP(p.x - q.x, self._p)
            r.x = (s ** 2 - p.x - q.x) % self._p
            r.y = ((p.y + s * (r.x - p.x)) * -1) % self._p
            if r.x < 0:
                r.x = r.x + self._p
            if r.y < 0:
                r.y = r.y + self._p
        elif (p.y + q.y) % self._p == 0:
            r = ZeroPoint()
        else:
            if p.y == 0:
                p, q = q, p
            s = (3 * p.x * p.x - self._a) * prime.invP(2 * p.y, self._p)
            r.x = (s ** 2 - 2 * p.x) % self._p
            r.y = ((p.y + s * (r.x - p.x)) * -1) % self._p
            if r.x < 0:
                r.x = r.x + self._p
            if r.y < 0:
                r.y = r.y + self._p
        return r
    def listPointGenerator(self):
        for i in range(self._p):
            for j in range(self._p):
                y2 = (i ** 3 - self._a * i  - self._b) % self._p
                if(j ** 2) % self._p == y2:
                    p = Point(i, j)
                    yield p
    def basePoint(self, start = None):
        if not start:
            start = self._p // 2
        for i in range(start, self._p):
            for j in range(self._p):
                y2 = (i ** 3 - self._a * i  - self._b) % self._p
                if(j ** 2) % self._p == y2:
                    p = Point(i, j)
                    return p
        return None
    def isInCurve(self, point):
        if isinstance(point, ZeroPoint):
            return True
        y2 = (point.y ** 2) % self._p
        t = (point.x ** 3 - self._a * point.x - self._b) % self._p
        return (y2 - t) % self._p == 0
