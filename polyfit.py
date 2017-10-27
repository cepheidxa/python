#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize
import itertools
import math
import random
import unittest

class PolyFit:
    def __init__(self, x, y, degree):
        if not isinstance(x, list) or not isinstance(y, list):
            raise ValueError('x and y should be a list')
        self.__x = x
        self.__y = y
        self.__degree = degree
        self.__coeffs = np.polyfit(self.__x, self.__y, self.__degree)
    def __polyfunc_one(self, x, coeffs):
        ret = 0
        degree = len(coeffs)
        for i in range(degree):
            ret += coeffs[i] * math.pow(x, degree -1 - i)
        return ret
    def polyfunc(self, x, coeffs):
        ret = []
        for element in x:
            ret.append(self.__polyfunc_one(element, coeffs))
        return ret
    def predict(self, x):
        if isinstance(x, list):
            return self.polyfunc(x, self.__coeffs)
        else:
            return self.__polyfunc_one(x, self.__coeffs)
    def plot(self, node = 10000):
        minx = min(self.__x)
        maxx = max(self.__x)
        step = (maxx - minx) / node
        x1 = np.arange(minx, maxx, step)
        fity = self.polyfunc(x1, self.__coeffs)
        plt.plot(self.__x, self.__y, 'o')
        plt.plot(x1, fity)
        plt.show()
    def printfunc(self):
        ret = []
        for i in range(self.__degree + 1):
            if i != 0:
                if self.__coeffs[self.__degree - i] > 0:
                    ret.append('+%f*x^%d'%(self.__coeffs[self.__degree - i], i))
                else:
                    ret.append('%f*x^%d'%(self.__coeffs[self.__degree - i], i))
            else:
                ret.append('%f'%(self.__coeffs[self.__degree - i]))
        print(''.join(ret))

class _Test(unittest.TestCase):
    def setUp(self):
        self.__static_PolyFit = PolyFit([1], [1], 1)
    def test_fit(self):
        x = list(range(100))
        y = list(range(100))
        solv = PolyFit(x, y, 5)
        for i in range(len(x)):
            self.assertTrue(abs(solv.predict(x[i]) - y[i]) < 0.0001)

        y = solv.polyfunc(x, [2,3,2])
        solv = PolyFit(x, y, 5)
        for i in range(len(x)):
            self.assertTrue(abs(solv.predict(x[i]) - y[i]) < 0.0001)
    def test_fit_random(self):
        for i in range(100):
            degree = random.randint(2, 4)
            datalen = random.randint(50, 100)
            x = list(np.random.random(datalen) * 100)
            coeffs = np.random.random(degree+1)
            y = list(self.__static_PolyFit.polyfunc(x, coeffs))
            solv = PolyFit(x, y, degree)
            fity = solv.predict(x)
            for j in range(len(x)):
                self.assertTrue(abs(fity[j]-y[j]) < 0.0001)
                self.assertTrue(abs(solv.predict(x[j])-y[j]) < 0.01)
    
if __name__ == '__main__':
    unittest.main()
