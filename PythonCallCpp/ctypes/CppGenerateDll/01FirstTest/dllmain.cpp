#include <stdio.h>
#include <iostream>

using namespace std;

#ifdef __cplusplus
	#define XEXT extern "C"
#else
	#define XEXT 
#endif // __cplusplus



#ifdef _WIN32		// 包含 win32 和 win64 
	#define LIB_API XEXT __declspec(dllexport)
#else				// Mac Linux
	#define LIB_API XEXT
#endif // _WIN32	



LIB_API void TestCtypes() {
	printf("In C TestCtypes\n");
}

LIB_API void TestCtypesNumber(int x, float y, bool isNum) {
	cout << x << " " << y << " " << isNum << endl;
	if (isNum) {
		cout << "True" << endl;
	}
	else
	{
		cout << "False" << endl;
	}
}


LIB_API void TestCtypesStringA(const char* str, int size) {
	cout << str << endl;
}

LIB_API void TestCtypesStringB(const wchar_t* w_str, int size) {
	// 暂时用C语言输出
	printf("%ls", w_str);
	//wcout << w_str << endl;	// 会乱码
}

