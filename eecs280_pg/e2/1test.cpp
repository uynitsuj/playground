#include <iostream>
using namespace std;



int main() {
int *x = new int(2);
int y_a = 3;
int *y = &y_a;
int *z = new int(4);
z = new int(5);
cout << *x << " " << *y << " " << *z << endl;
*x += *z;
*y -= *z;
delete x;
x = z;
cout << *x << " " << *y << " " << *z << endl;
delete x;
delete y;
delete z;

cout << *x << " " << *y << " " << *z << endl;
}