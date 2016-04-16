import unittest
import random
import prime

class Tests(unittest.TestCase):
    def test_isPrime(self):
        self.assertTrue(prime.isPrime(2))
        self.assertTrue(prime.isPrime(3))
        self.assertFalse(prime.isPrime(4))
        self.assertFalse(prime.isPrime(49))
        self.assertFalse(prime.isPrime(179426547))
        self.assertTrue(prime.isPrime(179426549))
    def test_getRandPrime(self):
        for i in range(100):
            n = prime.getRandPrime(10 + i)
            self.assertTrue(prime.isPrime(n))
    def test_inv(self):
        r = random.SystemRandom()
        for p in [prime.getRandPrime(10 + i) for i in range(10)]:
            self.assertEqual(prime.inv(1, p) % p, 1)
            self.assertEqual(prime.inv(p - 1, p) * (p - 1) % p, 1)
            for i in range(10):
                a = r.randint(1, p-1)
                self.assertEqual(prime.inv(a, p) * a % p, 1)
    def test_expmod(self):
        self.assertEqual(prime.expmod(5, 10, 11), 1)
        self.assertEqual(prime.expmod(15, 22, 23), 1)
        self.assertEqual(prime.expmod(24, 36, 37), 1)
        self.assertEqual(prime.expmod(35, 52, 53), 1)
        self.assertEqual(prime.expmod(50, 66, 67), 1)
    def test_sqrtmod(self):
        r = random.SystemRandom()
        for i in range(10):
            p = prime.getRandPrime(20)
            while p < 10:
                p = prime.getRandPrime(10)
            for j in range(100):
                a = r.randint(1, p - 1)
                x = prime.sqrtmod(a, p)
                if x:
                    self.assertTrue(x * x % p == a)
