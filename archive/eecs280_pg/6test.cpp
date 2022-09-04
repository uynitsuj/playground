#include <iostream>
#include <fstream>
#include <cstring>
using namespace std;
bool is_too_complex(const char* word, int threshold);

int main(int argc, char const *argv[])
{
    int threshold = stoi(argv[1]);
    ifstream fin;
    //cout << argv[2];
    fin.open(argv[2]);
    ofstream fout;
    //cout << argv[3];
    fout.open(argv[3]);
    string word;
    while(fin>>word){
        cout<<word;
        if (!is_too_complex(word.c_str(),threshold)){
            fout << word << " ";
        }
    }
    fin.close();
    fout.close();
    return 0;
}

bool is_too_complex(const char* word, int threshold) {
int complex_counter = 0;
const char *ptr = word;
while(*ptr){
    if(*ptr == 'a' 
    || *ptr == 'e'
    || *ptr == 'i'
    || *ptr == 'o'
    || *ptr == 'u'){ complex_counter++; }
    ptr++;
}
if(complex_counter > threshold) { return true;}
return false;
}