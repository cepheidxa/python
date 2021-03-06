#!/usr/bin/python3

import unittest
import ecc
from prime import getRandPrime
from random import SystemRandom
from logging import getLogger
from log import logger

class Tests(unittest.TestCase):
    def setUp(self):
        self._logger = getLogger('test.ecc')
    def test_basePoint(self):
        r = SystemRandom()
        for i in range(10):
            p = getRandPrime(5)
            while p <= 10:
                p = getRandPrime(5)
            e = ecc.ECC(r.randint(1, 100), r.randint(1, 100), p)
            G = e.G
            self.assertTrue(e.isInCurve(G))
    def test_listPointGenerator(self):
        r = SystemRandom()
        for i in range(10):
            p = getRandPrime(5)
            while p <= 10:
                p = getRandPrime(5)
            e = ecc.ECC(r.randint(1, 100), r.randint(1, 100), p)
            for point in e.listPointGenerator():
                self.assertTrue(e.isInCurve(point))
    def test_add(self):
        r = SystemRandom()
        for i in range(10):
            p = getRandPrime(5)
            while p <= 10:
                p = getRandPrime(5)
            e = ecc.ECC(r.randint(1, 100), r.randint(1, 100), p)
            all_points = list(e.listPointGenerator())
            for j in range(100):
                point1 = r.choice(all_points)
                point2 = r.choice(all_points)
                point = e.add(point1, point2)
                self.assertEqual(e.isInCurve(point), True)
