#include <cassert>
#include <iostream>
using namespace std;

int range(const int * array, int length);

int main(int argc, char const *argv[])
{
    int arr[] = {7, 13, 2, 8, 8, 5, 13};
    assert(range(arr, 7) == 11);
    cout << range(arr, 7);
    return 0;
}

int range(const int * array, int length){
    int max = *array;
    int min = *array;
    for (int i = 0; i < length; i++){
        if (max < *(array+i)){
            max = *(array+i);
        }
        if (min > *(array+i)){
            min = *(array+i);
        }
    }
    return max - min;
}