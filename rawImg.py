#!/usr/bin/env python3

import struct

class RawImgBMP128x64RGB565:
    def __init__(self, file):
        self.__width = 128
        self.__height = 64
        self.__header = b'BMF@\x00\x00\x00\x00\x00\x00F\x00\x00\x008\x00\x00\x00\x80\x00\x00\x00\xc0\xff\xff\xff\x01\x00\x10\x00\x03\x00\x00\x00\x00@\x00\x00\x13\x0b\x00\x00\x13\x0b\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf8\x00\x00\xe0\x07\x00\x00\x1f\x00\x00\x00\x00\x00\x00\x00'
        with open(file, 'rb') as fd:
            self.__contents = fd.read()
    def display(self, file):
        with open(file, 'w+b') as fd:
            fd.write(self.__header)
            fd.write(self.__contents)
    def displaybytes16bit(self, file):
        contents = ''
        for i in range(len(self.__contents)//2):
            if(i > 0 and i % 128 == 0):
                contents = contents + '\n'
            contents = contents + "%02x%02x "%(self.__contents[i * 2], self.__contents[i * 2 + 1])
        with open(file, 'w+b') as fd:
            fd.write(contents.encode())
    def displaybytes1bit(self, file):
        contents = self.toBlackWhite()
        result=''
        for i in range(len(contents)//2):
            if(i > 0 and i % 128 == 0):
                result = result + '\n'
            if(contents[i * 2] != 0):
                result = result + '1'
            else:
                result = result + '0'
        with open(file, 'w+b') as fd:
            fd.write(result.encode())
    def toBlackWhite(self):
        contents = list(self.__contents)
        for i in range(len(self.__contents)):
            if(contents[i // 2 * 2]!= 0):
                    contents[i//2 * 2] = 255
                    contents[i//2 * 2 + 1] = 255
            else:
                    contents[i//2 * 2] = 0
                    contents[i//2 * 2 + 1] = 0
        contents=bytes(contents)
        return contents
    def displayBlackWhite(self, file):
        """transfer the data in black-white format"""
        contents=self.toBlackWhite()
        with open(file, 'w+b') as fd:
            fd.write(self.__header)
            fd.write(contents)

if __name__ == "__main__":
    img = RawImgBMP128x64RGB565("b.raw")
    img.display("b.bmp")
    img.displayBlackWhite("c.bmp")
    img.displaybytes16bit("a.txt")
    img.displaybytes1bit("b.txt")
