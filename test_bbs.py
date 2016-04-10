import unittest
import bbs
from  random import SystemRandom
from math import sqrt

class Tests(unittest.TestCase):
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
        diff = abs(n - 2 * sum)
        self.assertEqual(diff/n < level * sigma, True)
        
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
        # 2 sigma , p = 95.45%
        # 3 sigma , p = 99.73%
        self.assertEqual(abs(sum / n - N / 2) < level * sigma_avarage, True)
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
