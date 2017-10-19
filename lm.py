#!/usr/bin/env python3
import math

def lm(y,x):
    """lm(y, x) -> -> beta0, beta2, sigma

    fit linear model with one variable"""
    if not isinstance(y, list) or not isinstance(x, list):
        raise ValueError('x and y must be list')
    if len(x) != len(y):
        raise ValueError('the length of x and y is not equal')
    mx = sum(x)/len(x)
    my = sum(y)/len(y)
    Sxx = sum(map(lambda e: (e - mx) ** 2, x))
    Sxy = sum(map(lambda e: (e[0] - mx) * (e[1] - my),zip(x, y)))
    beta1 = Sxy / Sxx
    beta0 = my - beta1 * mx
    sigma2 = sum(map(lambda e: (e[1] - beta0 - beta1 * e[0]) ** 2, zip(x, y))) / (len(x) - 2)
    return beta0, beta1, math.sqrt(sigma2)
    

if __name__ == '__main__':
    x = [0.1, 0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18, 0.20, 0.21, 0.23]
    y = [42.0, 43.5, 45.0, 45.5, 45.0, 47.5, 49.0, 53.0, 50.0, 55.0, 55.0, 60.0]
    r = lm(y, x)
    print(r)
