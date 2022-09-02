import os
from ctypes import *

lib = CDLL("FirstTest", winmode=0)

# 语法：(c_int * 10) (1,2,3,4,5,6,7,8,9,10)

# 语法2： a = [1, 2, 3]  (c_int * 10) (*a)

arr = [1, 2, 4, 5, 6]
arr_type = (c_int * len(arr))
arr_c = arr_type(*arr)
lib.TestArray.argtypes = (arr_type,)
lib.TestArray(arr_c, len(arr))
