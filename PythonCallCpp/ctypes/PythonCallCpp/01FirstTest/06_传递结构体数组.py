import os
from ctypes import *

lib = CDLL("FirstTest", winmode=0)


class Pos(Structure):
    _fields_ = [("x", c_int), ("y", c_int)]


pos_arr = [Pos(1, 1), Pos(2, 2), Pos(3, 3)]
pos_arr_type = Pos * len(pos_arr)
pos_arr_c = pos_arr_type(*pos_arr)

lib.TestStructArray.argtypes = (pos_arr_type,)
lib.TestStructArray(pos_arr_c, len(pos_arr_c))
print(type(pos_arr_c))      # <class '__main__.Pos_Array_3'>

print(pos_arr_c[0].x, pos_arr_c[0].y)       # 数组可以直接修改内部数据
print(pos_arr[0].x, pos_arr[0].y)           # 可以看出 pos_arr != pos_arr_c 的值









