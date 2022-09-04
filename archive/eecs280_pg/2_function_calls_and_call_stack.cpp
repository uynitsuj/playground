#include <iostream>
using namespace std;

int plus_one(int x) {
  return x + 1;
}

int plus_two(int x) {
  return plus_one(x + 1);
}

int main() {
  int result = 0;
  result = plus_one(0);
  result = plus_two(result);
  cout << result;             // prints 3
}

//At program startup, the main() function is called, 
//creating an activation record that holds the single local variable result
//declaration of result initializes its value to 0

//the program proceeds to call plus_one(0). 
//This creates an activation record for plus_one() that holds the parameter x

//he program initializes the value of x to the argument value 0 and runs the body of plus_one(). 
//The body computes the value of x + 1 by obtaining the value of x and adding 1 to it, 
//resulting in a value of 1, which the function then returns. 
//The return value replaces the original call to plus_one(0), 

//the activation record for plus_one is discarded before main() proceeds. 
//The code then assigns the return value of 1 to result

