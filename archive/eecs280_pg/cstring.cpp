#include <string>
#include <cassert>
#include <iostream>
using namespace std;
int main(){
    const int bruh = 6;
    char x[bruh] = "hello";
    //char b[] = "hello";
    //char y[] = {'h','e','l','l','o'};
    //string z = "hello";
    // determine behavior at this point
    //assert (x == b);
    //cout << y; // undefined behavior. This one prints out hello just fine
    for (int i=0;i<=bruh;i++){
        cout << *(x+i); //prints "hello"
    }
    cout<<endl;
    cout<< *(x+5); //prints nothing (in my implementation)

    assert(*(x+5) == 0); // true
}