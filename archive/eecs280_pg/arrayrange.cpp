#include <cassert>
#include <iostream>
using namespace std;

int range(const int * array, int length);
int search(int **arr, int length_outer, int length_inner);

int main(int argc, char const *argv[])
{
    int arr[] = {7, 13, 2, 8, 8, 5, 13};
    assert(range(arr, 7) == 11);
    cout << range(arr, 7);
    int arr1[] = {4, 4};
    int arr2[] = {7, 2};
    int arr3[] = {4, 3};
    int *a[] = {arr1, arr2, arr3};
    cout << search(a, 3, 2);
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

int search(int **arr, int length_outer, int length_inner){
    int cur_min_range = range(arr[0], length_inner);
    int min = 0;
    for (int i = 1; i< length_outer; i++){
        if(range(*(arr+i),length_inner) < cur_min_range){
            cur_min_range = range(*(arr+i),length_inner);
            min = i;
        }
    }
    return min;
}
