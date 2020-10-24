#include <cassert>
#include <iostream>
#include <cstring>
using namespace std;

// REQUIRES: 'array' is an array with 'size' elements
//           0 <= 'num_copies' && 'num_copies' <= 'size'
// MODIFIES: 'array'
// EFFECTS : Inserts the specified number of copies of the given item
//           into the beginning of the array. Existing elements are
//           shifted to the right, and those that shift off the end of
//           the array are discarded.
// EXAMPLE : int arr[5] = { 1, 2, 3, 4, 5 };
//           insert_multiple(arr, 5, 9, 3);
//           // arr now contains { 9, 9, 9, 1, 2 }
// NOTE: Drawing a picture will be very helpful for solving this problem.
void insert_multiple(int array[], int size, int item, int num_copies) {
assert(0 <= num_copies && num_copies <= size);
    for (int i = 0; i<num_copies; i++){
    for (int *ptr = array+size-1; ptr > array; ptr--){
        *ptr = *(ptr-1);
    }
    *array = item;
    }
}
// REQUIRES: str points to a valid C string.
// MODIFIES: str
// EFFECTS : Reverses the first k letters of str. If k is larger than
//           the length of the string, reverse the entire string.
// EXAMPLE : If str is "eels280", reverseSubstring(str, 5) modifies
//           str to become "2slee80".
// NOTE: You may use the strlen function from <cstring> if you need to.
void reverseSubstring(char* str, int k) {
    int l = strlen(str);
    if(k > l){
    k = l;
    }
    char temp;
    for (int i = 0; i < k/2; i++){
    temp = *(str+i);
    *(str+i) = *(str+k-i-1);
    *(str+k-i-1) = temp;
    }
}
int main(int argc, char const *argv[])
{
    int arr[5] = { 1, 2, 3, 4, 5 };
    insert_multiple(arr, 5, 9, 3);
    for(int i=0; i<5; i++){
        cout << *(arr + i);
    }
    char str[] = "eels280";
    reverseSubstring(str, 5);
    cout << str;
    return 0;
}
