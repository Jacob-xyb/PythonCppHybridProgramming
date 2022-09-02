import os
from ctypes import *

lib = CDLL("FirstTest", winmode=0)

print(lib.TestReturnInt())

# 字符串不指定就会输出整数
print(lib.TestReturnChar())
lib.TestReturnChar.restype = c_char_p
print(lib.TestReturnChar())     # byte

print(lib.TestReturnWChar())
lib.TestReturnWChar.restype = c_wchar_p
print(lib.TestReturnWChar())    # string

