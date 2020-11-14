#include <iostream>
using namespace std;

int main(int argc, char const *argv[])
{
    int arr[] = {1, 2, 3, 4, 5};
    //cout << &arr[2] << endl;
    //cout << &cout << &arr[2] + arr[0];
    //int *mystery = &arr[2] + arr[0];
    //int mystery1 = *arr;
    //int * mystery3 = &(&arr[3]);
    //int *mystery4 = arr;
    cout<< **arr;
    return 0;
}
