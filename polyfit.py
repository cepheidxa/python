#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
import random
import unittest

class PolyFit:
    def __init__(self, x, y, degree):
        self.__x = x
        self.__y = y
        self.__degree = degree
        self.__coeffs = np.polyfit(self.__x, self.__y, self.__degree)
        self.__p = np.poly1d(self.__coeffs)
    def predict(self, x):
        return self.__p(x)
    def plot(self, node = 10000):
        xp = np.linspace(np.min(self.__x), np.max(self.__x), node)
        plt.plot(self.__x, self.__y, 'o', xp, self.__p(xp),'-')
        plt.show()
    def printfunc(self):
        print(self.__p)
class _Test(unittest.TestCase):
    def test_fit(self):
        x = list(range(100))
        y = list(range(100))
        solv = PolyFit(x, y, 5)
        self.assertTrue(max(np.abs(solv.predict(x) - y)) < 0.0001)
    def test_fit_without_residuals(self):
        for i in range(10):
            degree = random.randint(2, 4)
            datalen = random.randint(50, 100)
            x = list(np.random.random(datalen) * 10)
            coeffs = np.random.random(degree+1)
            p = np.poly1d(coeffs)
            y = p(x)
            solv = PolyFit(x, y, degree)
            solv.printfunc()
            self.assertTrue(max(np.abs(solv.predict(x) - y)) < 0.001)
    def test_fit_with_residuals(self):
        for i in range(10):
            degree = random.randint(2, 4)
            datalen = random.randint(50, 100)
            x = list(np.random.random(datalen) * 10)
            coeffs = np.random.random(degree+1)
            p = np.poly1d(coeffs)
            residuals = np.random.random(datalen)*10 - 5
            y = p(x) + residuals
            solv = PolyFit(x, y, degree)
            solv.printfunc()
            #solv.plot(1000)
            self.assertTrue(max(np.abs(solv.predict(x) - y)) < np.max(np.abs(residuals)) * 1.5)
if __name__ == '__main__':
    unittest.main()
