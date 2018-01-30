#!/usr/bin/env python3

import ctypes
import enum

class tagBitMapFileHeader(ctypes.Structure):
    _pack_ = 1
    _fields_ =[('bfType', ctypes.c_uint16),
               ('bfSize', ctypes.c_uint32),
               ('bfReserved1', ctypes.c_uint16),
               ('bfReserved2', ctypes.c_uint16),
               ('bfOffBits', ctypes.c_uint32),
        ]

class BitMapInfoHeader(ctypes.Structure):
    _pack_ = 1
    _fields_ = [('biSize', ctypes.c_uint32),
                ('biWidth', ctypes.c_int32),
                ('biHeight', ctypes.c_int32),
                ('biPlanes', ctypes.c_uint16),
                ('biBitCount', ctypes.c_uint16),
                ('biCompression', ctypes.c_uint32),
                ('biSizeImage', ctypes.c_uint32),
                ('biXpelsPerMeter', ctypes.c_int32),
                ('biYpelsPerMeter', ctypes.c_int32),
                ('biClrUsed', ctypes.c_uint32),
                ('biClrImportant', ctypes.c_uint32)
        ]
#color space information
class tagRGBQUAD(ctypes.Structure):
    _pack_ = 1
    _fields_ = [('rgbBlue', ctypes.c_ubyte),
                ('rgbGreen', ctypes.c_ubyte),
                ('rgbRed', ctypes.c_ubyte),
                ('rgbReserved', ctypes.c_ubyte),
        ]

@enum.unique
class ImgColorType(enum.Enum):
    RGB565 = 1


t1 = tagBitMapFileHeader()
print('sizeof(tagBitMapFileHeader) =', ctypes.sizeof(t1))
t2 = BitMapInfoHeader()
print('sizeof(BitMapInfoHeader) =', ctypes.sizeof(t2))
t3 = tagRGBQUAD()
print('sizeof(tagRGBQUAD) =', ctypes.sizeof(t3))


def struct2stream(s):
    length = ctypes.sizeof()
    p = ctypes.cast(ctypes.pointer(s), ctypes.POINTER(ctypes.c_char*lenght))
    return p.contents.raw

def stream2struct(string, stype):
    length = ctypes.sizeof(stype)
    stream = (ctypes.c_char * length)()
    stream.raw = string
    p = ctypes.cast(stream,ctypes.POINTER(stype))
    return p.contents

#a = stream2struct(b'BMF@\x00\x00\x00\x00\x00\x00F\x00\x00',tagBitMapFileHeader)
#b = stream2struct(b'8\x00\x00\x00\x80\x00\x00\x00@\x00\x00\x00\x01\x00\x10\x00\x03\x00\x00\x00\x00@\x00\x00\x13\x0b\x00\x00\x13\x0b\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',BitMapInfoHeader)
#c1 = stream2struct(b'\x00\xf8\x00\x00', tagRGBQUAD)
#c2 = stream2struct(b'\xe0\x07\x00\x00', tagRGBQUAD)
#c3 = stream2struct(b'\x1f\x00\x00\x00', tagRGBQUAD)
#c4 = stream2struct(b'\x00\x00\x00\x00', tagRGBQUAD)
class BmpHeader:
    def __init__(self, width, heigh, type):
        if type == ImgColorType.RGB565:
            self.__t1 = tagBitMapFileHeader()
            self.__t2 = BitMapInfoHeader()
            self.__t1.bfType = 0x4D42;
            self.__t1.bfSize = width * heigh * 2 + ctypes.sizeof(t1) + ctypes.sizeof(t2) + 16;
            self.__t1.bfReserved1 = 0
            self.__t1.bfReserved2 = 0
            self.__t1.bfOffBits = 70
            self.__t2.biSize = 56
            self.__t2.biWidth = width
            self.__t2.biHeight = heigh
            self.__t2.biPlanes = 1
            self.__t2.biBitCount = 16
            self.__t2.biCompression = 3
            self.__t2.biSizeImage = width * heigh * 2
            self.__t2.biXpelsPerMeter = 0
            self.__t2.biYpelsPerMeter = 0
            self.__t2.biClrUsed = 0
            self.__t2.biClrImportant = 0
        else:
            raise ValueError('Unkown code type')
    @property
    def tagBitMapFileHeader(self):
        return self.__t1
    @property
    def BitMapInfoHeader(self):
        return self.__t2
    @property
    def tagRGBQUAD_x4(self):
        return b'\x00\xff\x00\x00\x00\xff\x00\x00\xff\x00\x00\x00\x00\x00\x00\x00'

class RawImgBMPRGB565():
    def __init__(self, width, height, file):
        self.__width = width
        self.__height = height
        self.__type = ImgColorType.RGB565
        self.__header = BmpHeader(self.__width, self.__height, self.__type)
        with open(file, 'rb') as fd:
            self.__contents = fd.read()
    def display(self, file):
        with open(file, 'w+b') as fd:
            fd.write(self.__header.tagBitMapFileHeader)
            fd.write(self.__header.BitMapInfoHeader)
            fd.write(self.__header.tagRGBQUAD_x4)
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
    img = RawImgBMPRGB565(640, 400, "1.raw")
    img.display("b.bmp")
    #img.displayBlackWhite("c.bmp")
    #img.displaybytes16bit("a.txt")
    #img.displaybytes1bit("b.txt")
    pass
