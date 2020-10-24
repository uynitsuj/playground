#include <iostream>
using namespace std;

void increment(int &num, int inc);

int* foo(int x, int& y){
    increment(y, x);
    return &y;
}

int main(){
    int a = 1; // assume a is allocated at address 0x10
    int& b = a;
    int x = 10; // assume x is allocated at address 0x20
    int& y = x;

    int *f1 = foo(a,b); // assume f1 is allocated at address 0x30
    int *f2 = foo(x,y); // assume f2 is allocated at address 0x40
    *f2 += 100;

    cout << a << endl;
    cout << b << endl;
    cout << x << endl;
    cout << y << endl;
    cout << f1 << endl;
    cout << f2 << endl;
}

void increment(int &num, int inc){
    num += inc;
}