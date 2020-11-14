#include <iostream>
using namespace std;

int main(int argc, char const *argv[])
{
    int x  = 5;
    int *ptr = &x;
    int b = *&x;
    
    int *huh = &*ptr;

    int **dubl = &ptr;

    int arr[]={4,5};
    int *mat[] = {arr};

    cout << b << endl;
    cout << huh << endl;
    cout << *huh << endl;
    cout << dubl << endl;
    cout << *dubl << endl;
    cout << **dubl << endl;
    cout << mat <<endl;
    cout << *mat[0] <<endl;
    cout << *mat[0]+1 <<endl;

    return 0;
}
