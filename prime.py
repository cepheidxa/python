#!/usr/bin/python3

from ctypes import *
import random
import logging
import log

logger = logging.getLogger('test.prime')

__all__ = ['isPrime', 'getRandPrime', 'inv']

libgmp = CDLL('libgmp.so.10')

class _mpz_t(Structure):
    _fields_ = [('_mp_alloc', c_int), ('_mp_size', c_int), ('_mp_d', POINTER(c_ulong))]

def _mpz_init_set_str(p, s, base):
    libgmp.__gmpz_init_set_str(pointer(p), s, base)

def _mpz_probab_prime_p(p, reps):
    return libgmp.__gmpz_probab_prime_p(pointer(p), reps)

def isPrime(n):
    """Test if n is a prime."""
    if type(n) != int:
        raise ValueError('type error, n should be int type')
    v = _mpz_t()
    _mpz_init_set_str(v, bytes(str(n), encoding = 'ascii'), 10)
    if _mpz_probab_prime_p(v, 50) == 0:
        return False
    else:
        return True

def getRandPrime(bits = 1024):
    """Get a random prime."""
    r = random.SystemRandom()
    v = r.getrandbits(bits)
    while not isPrime(v):
        v = r.getrandbits(bits)
    return v

def inv(v, p):
    v = v % p
    if v < 0:
        v = v + p
    if v == 0:
        raise ValueError('v should not be zero in inv')
    elif v == 1:
        return 1
    pp, vv = p, v
    a, b = divmod(pp, vv)
    l1=[1,0]
    l2 = [0, 1]
    l3 = list(map(lambda x: x[0] - a * x[1], zip(l1, l2)))
    while b != 1:
        pp, vv = vv, b
        a, b = divmod(pp, vv)
        l1 = l2
        l2 = l3
        l3 = list(map(lambda x: x[0] - a * x[1], zip(l1, l2)))
    ret = l3[1]
    ret = ret % p
    if ret < 0:
        ret = ret + p
    return ret

def expmod(x, n, p):
    b = n
    t = x % p
    ret = 1
    while b != 0:
        if b & 0x1 != 0:
            ret *= t
            ret %= p
        t = t * t % p
        b >>= 1
    return ret


def isQR(a, p):
    """is a a quadratic residule mod p, p must be a prime
       if p is prime, and (a, p) = 1, then

       a is a a quadratic residule of p is eaual to
       a ** ((p-1)/2) = 1 mod p

       a is not a a quadratic residule of p is eaual to
       a ** ((p-1)/2) = -1 mod p
    """
    if not isPrime(p):
        raise ValueError('p must be prime in sqrtmod in module {0}'.format(__name__))
    return expmod(a, (p - 1)>>1, p) == 1

def sqrtmod(a, p):
    """Get x where x^2 = a mod p, p must be a prime

       Cipolla's algorithm, refered to Wikipedia
    """
    if not isPrime(p):
        raise ValueError('p must be prime in sqrtmod in module {0}'.format(__name__))
    if isQR(a, p) == False:
        return None
    r = random.SystemRandom()
    while True:
        b = r.randint(1, p-1)
        if b * b % p == a % p:
            return b
        if isQR((b * b - a) % p, p) == False:
            break
    #define y, y**2 = 5， get solution in Fp(y) filed
    t = [b, 1]
    y2 = (b * b - a) % p
    q = (p + 1) >> 1
    ret = [1, 0]
    while q != 0:
        if q & 0x01 != 0:
            ret = [(ret[0] * t[0] + y2 * ret[1] * t[1]) % p, (ret[0] * t[1] + ret[1] * t[0]) % p]
        t = [(t[0] * t[0] + y2 * t[1] * t[1]) % p, 2 * t[0] * t[1] % p]
        q >>= 1
    if ret[1]:
        logger.error('sqrt({0}, {1}), b = {2}, ret=({3}, {4})'.format(a, p, b, ret[0], ret[1]))
    return ret[0]
