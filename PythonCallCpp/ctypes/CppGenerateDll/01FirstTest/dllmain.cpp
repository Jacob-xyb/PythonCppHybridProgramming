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


#pragma region 第一次尝试

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

LIB_API void TestCtypesStringBuffer(char* str, int size) {
	//可更改的字符串
	str[0] = '@';
	str[1] = '#';
	str[2] = '\0';		// 字符串结尾
	cout << str << endl;
}

LIB_API void TestCtypesStringB(const wchar_t* w_str, int size) {
	// 暂时用C语言输出
	printf("%ls", w_str);
	//wcout << w_str << endl;	// 会乱码
}
#pragma endregion


#pragma region 测试返回值

LIB_API int TestReturnInt() {
	return 1018;
}

LIB_API const char * TestReturnChar() {
	return "TestReturnChar String";
}

LIB_API const wchar_t* TestReturnWChar() {
	return L"TestReturnWChar String";
}

#pragma endregion


#pragma region 传递和返回指针

LIB_API int* TestPointer(float* f1) {
	static int re = 1001;
	*f1 = 99.99f;
	return &re;
}

#pragma endregion


#pragma region 传递数组

LIB_API void TestArray(int* arr, int size)
{
	for (int i = 0; i < size; i++)
	{
		printf("%d ", arr[i]);
	}
}

#pragma endregion


#pragma region 传递和返回结构体

struct Pos
{
	int x;
	int y;
};


LIB_API void TestStruct(Pos pos) {
	printf("pos x = %d y = %d\n", pos.x, pos.y);
	pos.x += 10;
	pos.y += 10;
}

LIB_API void TestStructPointer(Pos* pos) {
	printf("pos x = %d y = %d\n", pos->x, pos->y);
	pos->x += 20;
	pos->y += 20;
}

LIB_API void TestStructReference(Pos& pos) {
	printf("pos x = %d y = %d\n", pos.x, pos.y);
	pos.x += 30;
	pos.y += 30;
}

LIB_API void TestStructArray(Pos* pos_arr, int size) {
	for (int i = 0; i < size; i++)
	{
		printf("%d %d\n", pos_arr[i].x, pos_arr[i].y);
	}
	// 尝试修改第一个数组
	pos_arr[0].x = -1;
	pos_arr[0].y = -1;
}

LIB_API Pos* TestReturnStructPointer() {
	static Pos pos;
	pos.x = 10;
	pos.y = 20;
	return &pos;
}

#pragma endregion



