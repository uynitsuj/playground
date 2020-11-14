#include <iostream>
#include <string>
using namespace std;
struct Zoom {
    int meeting_id; 
    string meeting_name; 
    string participants_list[50];
    int number_of_participants;
};

int Zoom_first_x_students(const Zoom * z, int x, string *arr);

int main(int argc, char const *argv[])
{
    int arr[] = {1, 2, 3, 4, 5};
    cout << &arr[2] << endl;
    cout << &cout << &arr[2] + arr[0];
    int *mystery = &arr[2] + arr[0];
    int mystery1 = *arr;
    //int * mystery3 = &(&arr[3]);
    int *mystery3 = arr;
    cout<<**arr;
   Zoom z = {1, "eecs280_oh", {"christina", "jon", "nicole", "sofia"}, 4};
   string arr[3];
   cout << Zoom_first_x_students(&z, 2, arr);
   cout << *arr << " " << *(arr+1) <<
   " " << *(arr+2) << endl;

    return 0;
}


int Zoom_first_x_students(const Zoom * z, int x, string *arr) {
int counter = 0;
if (x > z->number_of_participants) {x = z->number_of_participants;}
for (int i = 0; i < x; i++){
    *(arr+i) = *(z->participants_list+i);
    counter++;
}
return counter;
}
