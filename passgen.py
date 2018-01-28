#!/usr/bin/python3

from argparse import ArgumentParser
from secrets import SystemRandom
from string import ascii_lowercase, ascii_uppercase, digits, punctuation

if __name__ == "__main__":
    parser = ArgumentParser(description = "Generate random password.")
    parser.add_argument("-n",action = 'store_true', help = "Have numberss in the passwrod")
    parser.add_argument("-a",action = 'store_true', help = "Have lowercase characters in the passwrod")
    parser.add_argument("-A",action = 'store_true', help = "Have uppercase characters in the passwrod")
    parser.add_argument("-s",action = 'store_true', help = "Have symbols in the passwrod")
    parser.add_argument("-l", type = int, metavar= "length", help = "The length of password", default = 16)
    command = parser.parse_args()

    r = SystemRandom()
    password = [] 
    valid_chars = ''
    if command.n:
        valid_chars += digits
    if command.a:
        valid_chars += ascii_lowercase
    if command.A:
        valid_chars += ascii_uppercase
    if command.s:
        valid_chars += punctuation
    if not valid_chars:
        valid_chars = digits
    print("".join([r.choice(valid_chars) for i in range(command.l)]))
