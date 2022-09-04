#include <iostream>

int main(int argc, char const *argv[])
{
    const int a = 5;
    //a = 4; ERROR: "expression must be a modifiable lvalue"
    
    //int * ptr = &a; ERROR: "a value of type "const int *" cannot be used to initialize an entity of type "int *""
    //*ptr = 4;
    //int &ref = a; ERROR: "qualifiers dropped in binding reference of type "int &" to initializer of type "const int""

    int x = 3;
    int const &ref = x;      // OK -- does not permit const object to be modified
    const int *ptr = &x;     // OK -- does not permit const object to be modified
    int *ptr1 = &x;          // OK -- does not permit const object to be modified
    const int *ptr2 = ptr1;  // OK -- does not permit const object to be modified
    //ptr1 = ptr2;              ERROR -- compiler sees that ptr2 is pointing to a
                             //          a const object, but ptr1 is not a pointer
                             //          to const

    return 0;
}
