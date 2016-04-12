import unittest
import bbs
from  random import SystemRandom
from math import sqrt
import log
import logging

class Tests(unittest.TestCase):
    def setUp(self):
        self._logger = logging.getLogger('test.bbs')
    def run_test_bits(self, r, level):
        """Test based on Norm distribution
            Xi ~ 1, or -1 with equal possibility
            X = (X1 + ... + Xn) / n
            E(Xi) = 0
            E(Xi^2)=  1
            Var(X) = Var(Xi)/n = 1 / n
            set n = 10000
            EX = 0
            Var(X) = 0.0001
        """ 
        sum = 0
        n = 1000
        r2 = SystemRandom()
        r.seed(r2.getrandbits(1024))
        sigma = 1 / sqrt(n)
        for i in range(n):
            sum = sum + r.getrandbits(1)
        diff = abs(n - 2 * sum) / n
        self._logger.debug('diff is {0} sigma'.format(diff/sigma))
        # 2 sigma , p = 95.45%
        # 3 sigma , p = 99.73%
        self.assertEqual(diff < level * sigma, True)
        
    def run_test_avarage(self, r, level):
        """Test based on Norm distribution
            Xi ~ Norm([0, N])
            X = (X1 + ... + Xn) / n
            E(Xi) = N / 2
                     2(N+1)(N+2) - 3(N+1)
            E(Xi^2)=  --------------------
                              6
            Var(X) = Var(Xi)/n = [E(Xi^2) - (EXi)^2 ] / n
            set n = 10000 N = 100
            EX = 50
            Var(X) = 0.08835
        """ 
        sum = 0
        N = 100
        n = 1000
        for i in range(n):
            sum = sum + r.randint(0, N)
        EXi = N / 2
        EXiXi = (2 * (N + 1) * (N + 2) - 3 * (N + 1))/6
        sigma_avarage = sqrt((EXiXi ** 2 - EX ** 2) / n)
        diff = abs(sum / n - N / 2)
        # 2 sigma , p = 95.45%
        # 3 sigma , p = 99.73%
        self._logger.debug('diff is {0} sigma'.format(diff/sigma))
        self.assertEqual(diff < level * sigma_avarage, True)
    def test_BBS256(self):
        #self.run_test_avarage(bbs.BBS256(), 3)
        self.run_test_bits(bbs.BBS256(), 3)
    def test_BBS512(self):
        #self.run_test_avarage(bbs.BBSi512(), 3)
        self.run_test_bits(bbs.BBS512(), 3)
    def test_BBS1024(self):
        #self.run_test_avarage(bbs.BBS1024(), 3)
        self.run_test_bits(bbs.BBS1024(), 3)
    def test_BBS4096(self):
        #self.run_test_avarage(bbs.BBS4096(), 3)
        self.run_test_bits(bbs.BBS4096(), 3)
