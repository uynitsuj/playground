#include <iostream>
using namespace std;

int main(int argc, char const *argv[])
{
    int a = 5;
    int *ptr = &a;
    int * &p = ptr;
    cout << p << endl;
    cout << ptr << endl;
    const char *arr[] = { "hello", "world", "lobster"};
    cout << arr[1] + 2 << endl;
    cout << (*(arr + 2))[4] << endl;
    return 0;
}
