//When the program runs, execution starts at main(). 
//For each of the variables declared within main(), 
//the value of the variable is stored in some memory location. 
//Consider a basic machine model where memory is represented as a big array, 
//with each index in the array corresponding to a memory location that can hold a value

int main() {
  int x = 3;
  double y = 4.1;
  int z = x;
  x = 5;
  //these variables exist only within this scope
}

//modifes the value of the object that x is referring to
void value_semantics() {
  int x = 42;    // initialize value of x to 42
  int y = 99;    // initialize value of y to 99
  x = y;         // assign value of y to value of x
}

//modifies which object y is referring to
void reference_semantics() {
  int x = 42;  // initialize value of x to 42
  int z = 3;   // initialize value of z to 3
  int &y = x;  // y and x are now names for the same object
  x = 24;      // assigns 24 to object named x/y
  y = z;       // Does NOT re-bind y to a different object
               // Value semantics used here.
}
//C++ supports reference semantics only when initializing a new variable with the use of the ampersand