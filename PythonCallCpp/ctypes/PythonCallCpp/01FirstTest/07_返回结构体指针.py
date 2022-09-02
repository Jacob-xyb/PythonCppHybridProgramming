import os
from ctypes import *

lib = CDLL("FirstTest", winmode=0)


class Pos(Structure):
    _fields_ = [("x", c_int), ("y", c_int)]


lib.TestReturnStructPointer.restype = POINTER(Pos)
pos = lib.TestReturnStructPointer()

print(pos)              # 指针对象：<__main__.LP_Pos at 0x1c8ab1e6240>
print(pos.contents)     # 指针所指的实例对象：<__main__.Pos at 0x1c8ab1e64c0>
print(pos.contents.x, pos.contents.y)

