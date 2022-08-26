# C++编译动态库

## Windows

- dll 动态链接库
- _declspec(dllexport)
- extern "C"
- 库在系统目录或当前执行目录
- dll 加载路径与Python库查找路径无关（sys.path)

### Python的限制

**FileNotFoundError: Could not find module ‘xxx.dll’. (or one of its dependencies). Try using the full path with constructor syntax.**

原因：自python3.8开始，考虑到dll劫持等安全性问题，python3.8更改了dll的搜索加载机制，即只在指定可行的位置搜索加载dll，不再自动读取系统的**环境变量**Path了。

**解决方法**

- 方法1

老老实实使用完整的绝对路径,
如果还不行，说明这个dll依赖了其他路径下的dll，这种情况使用方法2添加路径

```python
CDLL("xxx/yyy/zzz.dll")
WinDLL("xxx/yyy/zzz.dll")
```

- 方法2

添加dll及其所有依赖的搜索路径（绝对路径）再加载

```python
os.add_dll_directory("xxx/yyy")
CDLL("zzz.dll")
```

- 方法3（推荐）

在加载时加上参数`winmode=0`，此参数为py38的参数，为了兼容3.8以下，3.8以前的没有这个参数。
**此方法能够使用相对路径 加载工程下的dll 或者 加载环境变量Path下的dll**

指定winmode参数（该参数将指定底层调用WinAPI LoadLibraryEx时所使用的flags），将值指定为0可以从本地路径加载，替换掉默认行为。

```python
CDLL("yyy/zzz.dll", winmode=0)
WinDLL("yyy/zzz.dll", winmode=0)
```

# ctypes 基础

## 类型对应

![image-20220826133242823](https://s2.loli.net/2022/08/26/Rm4b8lwyd6ZgSc5.png)

### 传递字符串

| python函数              | C++类型 |
| ----------------------- | ------- |
| c_wchar_p()  # 默认转换 | string  |
| c_char_p()              | byte    |
| create_string_buffer    |         |

