import os
from ctypes import *

lib = CDLL("FirstTest", winmode=0)

# pointer 返回实例
# POINTER 返回类型
# byref(x [, offset])

f1 = c_float(66.66)
lib.TestPointer.argtypes = (POINTER(c_float),)
lib.TestPointer.restype = POINTER(c_int)

# 指针的内容可以访问可以修改
int1 = lib.TestPointer(f1)      # 指针.contents.value
print(f1.value)
print(int1.contents.value)



