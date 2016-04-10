#!/usr/bin/python3

from ctypes import *
import random

__all__ = ['isPrime', 'getRandPrime', 'invP']

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

def invP(v, p):
    v = v % p
    if v < 0:
        v = v + p
    if v == 0:
        raise ValueError('v should not be zero in invP')
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


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--bits', type = int, default = 10, help= 'the lenght of bits')
    command = parser.parse_args()
    for i in range(5):
        p = getRandPrime(command.bits)
        print(p)
