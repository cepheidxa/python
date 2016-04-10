import unittest
import random
import prime

class Tests(unittest.TestCase):
    def test_isPrime(self):
        self.assertEqual(prime.isPrime(2), True)
        self.assertEqual(prime.isPrime(3), True)
        self.assertEqual(prime.isPrime(4), False)
        self.assertEqual(prime.isPrime(49), False)
        self.assertEqual(prime.isPrime(179426547), False)
        self.assertEqual(prime.isPrime(179426549), True)
    def test_getRandPrime(self):
        for i in range(100):
            n = prime.getRandPrime(10 + i)
            self.assertEqual(prime.isPrime(n), True)
    def test_invP(self):
        r = random.SystemRandom()
        for p in [prime.getRandPrime(10 + i) for i in range(10)]:
            self.assertEqual(prime.invP(1, p) % p, 1)
            self.assertEqual(prime.invP(p - 1, p) * (p - 1) % p, 1)
            for i in range(10):
                a = r.randint(1, p-1)
                self.assertEqual(prime.invP(a, p) * a % p, 1)
