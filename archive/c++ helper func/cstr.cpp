#include "cstr.h"

int strlen(const char* str) {
    int size = 0;
    while(*str++) size++;
    return size;
}