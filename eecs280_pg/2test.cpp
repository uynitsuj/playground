#include <iostream>
#include <ifstream>
using namespace std;

int main(int argc, char const *argv[])
{
    int threshold = stoi(argv[1]);
    ifstream fin;
    fin.open(argv[2]);
    ofstream fout;
    fout.open(argv[3]);
    string word;
    while(fin>>word){
        if (!is_too_complex(word.c_str(),threshold)){
            fout << word;
        }
    }
    fin.close();
    fout.close();
}
