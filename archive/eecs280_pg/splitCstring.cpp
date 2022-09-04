#include <iostream>
using namespace std;

void split_string(char *dst, const char*src, int pos);

int main(int argc, char const *argv[])
{
    char dst[10];
    split_string(dst, "hello", 2);
    cout << dst << endl;
    return 0;
}

void split_string(char *dst, const char*src, int pos){
    const char* first = src;
    const char* split = src + pos;
    for (; *split;split++){
        *dst = *split;
        dst++;
    }
    for (int i = 0; i<pos; i++){
        *dst = *first;
        dst++;
        first++;
    }
    *dst = '\0';
}
