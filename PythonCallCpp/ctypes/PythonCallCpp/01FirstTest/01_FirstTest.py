import os
from ctypes import *

lib = CDLL("FirstTest", winmode=0)
lib.TestCtypes()

lib.TestCtypesNumber(100, c_float(99.1), True)

# 传递 byte
s1 = "hello world"
lib.TestCtypesStringA(c_char_p(s1.encode()), len(s1))
lib.TestCtypesStringA(s1.encode(), len(s1))     # 同样正常生效

s1_buffer = create_string_buffer(100)
lib.TestCtypesStringBuffer(s1_buffer)
# buffer.raw: 原始值 ; buffer.value: 真实值 ; len(buffer): 长度
py_str = s1_buffer.raw.decode().rstrip('\x00')
print(f"python: {s1_buffer.value.decode()}")


# 传递 string: wchar_t 但是 C++ 只能 printf 输出 不然乱码
s2 = "Jacob-xyb"
lib.TestCtypesStringB(c_wchar_p(s2), len(s2))

s3 = "std::string"
# lib.TestCtypesStringC(create_string_buffer(s3.encode()), len(s3))



