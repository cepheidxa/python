#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import random
import unittest


def func(x, a, b, c):
    y = a * np.sin(b * x + c)
    return y

x = np.linspace(1, 10, 100)
y = 2 * np.sin(3 * x + 4)
y_noise = np.random.random(100) - 0.5
y += y_noise

popt, pcov = curve_fit(func, x, y, bounds = (1,[200,5,5]))
plt.plot(x, y, 'o', x, func(x, *popt), '-')
plt.show()

if __name__ == '__main__':
    #unittest.main()
    pass
