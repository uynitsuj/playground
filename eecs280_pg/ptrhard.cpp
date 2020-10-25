#include <iostream>
using namespace std;

int main(int argc, char const *argv[])
{
    int a = 5;
    int *ptr = &a;
    int * &p = ptr;
    cout << p << endl;
    cout << ptr << endl;
    return 0;
}
