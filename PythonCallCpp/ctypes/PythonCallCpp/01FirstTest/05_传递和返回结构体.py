import os
from ctypes import *

# class Pos(Structure):
#   _fields_ = [("x", c_int), ("y", c_int)]
lib = CDLL("FirstTest", winmode=0)


class Pos(Structure):
    _fields_ = [("x", c_int), ("y", c_int)]


print("====对象作为参数====：")
pos1 = Pos(1, 1)
lib.TestStruct.argtypes = (Pos,)
lib.TestStruct(pos1)
print(f"修改后的值：{pos1.x} {pos1.y}")


print("====指针作为参数====：")
pos2 = Pos(2, 2)
lib.TestStructPointer.argtypes = (POINTER(Pos),)
lib.TestStructPointer(pos2)                 # 直接传入类也可以修改值
print(f"修改后的值：{pos2.x} {pos2.y}")
lib.TestStructPointer(byref(pos2))
print(f"修改后的值：{pos2.x} {pos2.y}")

print("====引用作为参数====：")
pos3 = Pos(3, 3)
lib.TestStructReference.argtypes = (POINTER(Pos),)
lib.TestStructReference(pos3)               # 引用：指定类型为指针 可以直接修改值
print(f"修改后的值：{pos3.x} {pos3.y}")
lib.TestStructReference(byref(pos3))        # 引用：传入指针也可以直接修改值
print(f"修改后的值：{pos3.x} {pos3.y}")

