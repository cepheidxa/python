#!/usr/bin/python3

import unittest
import ecc
from prime import getRandPrime
from random import SystemRandom

class Tests(unittest.TestCase):
    def test_basePoint(self):
        r = SystemRandom()
        for i in range(10):
            p = getRandPrime(10)
            while p <= 10:
                p = getRandPrime(10)
            e = ecc.ECC(r.randint(1, 1000), r.randint(1, 1000), getRandPrime(10))
            self.assertEqual(e.isInCurve(e.G), True)
    def test_listPointGenerator(self):
        r = SystemRandom()
        for i in range(10):
            p = getRandPrime(10)
            while p <= 10:
                p = getRandPrime(10)
            e = ecc.ECC(r.randint(1, 1000), r.randint(1, 1000), getRandPrime(10))
            for point in e.listPointGenerator():
                self.assertEqual(e.isInCurve(point), True)
    def test_add(self):
        r = SystemRandom()
        for i in range(10):
            p = getRandPrime(10)
            while p <= 10:
                p = getRandPrime(10)
            e = ecc.ECC(r.randint(1, 1000), r.randint(1, 1000), getRandPrime(10))
            all_points = list(e.listPointGenerator())
            for j in range(100):
                point1 = r.choice(all_points)
                point2 = r.choice(all_points)
                point = e.add(point1, point2)
                self.assertEqual(e.isInCurve(point), True)
