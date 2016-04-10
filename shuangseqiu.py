#!/usr/bin/python3

import random2

class ShuangSeQiu:
    def __init__(self):
        self.__r = random2.Random()
    def randRed(self):
        return self.__r.randint(1, 33)
    def randBlue(self):
        return self.__r.randint(1, 16)
    def cast(self):
        red = set()
        while len(red) < 6:
            red.add(self.randRed())
        blue = self.randBlue()
        return (sorted(red), blue)
            
if __name__ == "__main__":
    a = ShuangSeQiu()
    for i in range(2):
        print(a.cast())
