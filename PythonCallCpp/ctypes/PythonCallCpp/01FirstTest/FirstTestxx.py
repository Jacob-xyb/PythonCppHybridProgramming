import os
from ctypes import *

lib = CDLL("FirstTest", winmode=0)
lib.TestCtypes()

lib.TestCtypesNumber(100, c_float(99.1), True)

s1 = "hello world"
lib.TestCtypesStringA(c_char_p(s1.encode()), len(s1))

s2 = "Jacob-xyb"
lib.TestCtypesStringB(s2, len(s2))
