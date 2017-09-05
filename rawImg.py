#!/usr/bin/env python3

import struct

class RawImgBMP128x64RGB565:
    def __init__(self, file):
        self.__width = 128
        self.__height = 64
        self.__header = b'BM\x8a@\x00\x00\x00\x00\x00\x00\x8a\x00\x00\x00|\x00\x00\x00\x80\x00\x00\x00@\x00\x00\x00\x01\x00\x10\x00\x03\x00\x00\x00\x00@\x00\x00\x13\x0b\x00\x00\x13\x0b\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf8\x00\x00\xe0\x07\x00\x00\x1f\x00\x00\x00\x00\x00\x00\x00BGRs\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        with open(file, 'rb') as fd:
            self.__contents = fd.read()
    def display(self, file):
        with open(file, 'w+b') as fd:
            fd.write(self.__header)
            fd.write(self.__contents)

    def displayBlackWhite(self, file):
        """transfer the data in black-white format"""
        contents = list(self.__contents)
        for i in range(len(self.__contents)):
            if(contents[i // 2 * 2]!= 0 or contents[i // 2 * 2 + 1] != 0):
                    contents[i//2 * 2] = 255
                    contents[i//2 * 2 + 1] = 255
        contents=bytes(contents)
        with open(file, 'w+b') as fd:
            fd.write(self.__header)
            fd.write(contents)

if __name__ == "__main__":
    img = RawImgBMP128x64RGB565("a.raw")
    img.display("b.bmp")
    img.displayBlackWhite("c.bmp")
