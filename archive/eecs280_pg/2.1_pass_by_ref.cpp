#include <iostream>
using namespace std;

void swap(int &x, int &y) {
  int tmp = x;
  x = y;
  y = tmp;
}

int main() {
  int a = 3;
  int b = 7;
  cout << a << ", " << b << endl;  // prints 3, 7
  swap(a, b);
  cout << a << ", " << b << endl;  // prints 7, 3
}
//The program starts by creating an activation record for main(), 
//with space for the local variables a and b. 

//It initializes a to 3 and b to 7 and then prints out their values. 
//The program then calls swap(a, b), which evaluates the expressions a and b to obtain their objects, 
//creates an activation record for swap(), and initializes the parameters from the argument objects. 
//Since the two parameters are references, the activation record does not contain user-accessible 
//memory for the parameters. (The metadata for the function, however, may include information about the parameters.) 