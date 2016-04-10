#!/usr/bin/python3

from argparse import ArgumentParser
from random import SystemRandom
from string import ascii_letters, digits, punctuation

if __name__ == "__main__":
    parser = ArgumentParser(description = "Generate random password.")
    parser.add_argument("-s",action = 'store_true', help = "Have symbols in the passwrod")
    parser.add_argument("-l", type = int, metavar= "length", help = "The length of password", default = 16)
    command = parser.parse_args()

    r = SystemRandom()
    password = [] 
    valid_chars = ascii_letters + digits
    if command.s:
        valid_chars = valid_chars + punctuation
    print("".join([r.choice(valid_chars) for i in range(command.l)]))
