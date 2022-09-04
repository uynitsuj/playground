#include <cassert>
#include <string>
#include <iostream>
#include <fstream>
using namespace std;


// REQUIRES: email is a non-empty c-string containing exactly
//           one '@' and one '.' 
//          '@' always occurs before the '.'
//           domain is a non-empty c-string and does not contain '.'
// EFFECTS:  Returns true if email has the format 
//           <username>@<domain>.<extension>
//           where <username> and <extension> are allowed to be empty
// EXAMPLES: 
//       is_valid_email("audladd@umich.edu", "umich") -> true
//       is_valid_email("jbbeau@gmail.com", "gmail")  -> true
//       is_valid_email("nathanmp@aol.net", "umich")  -> false
//       is_valid_email("cjtalof@umich", "umich")     -> false
//       is_valid_email("@umich.", "umich")           -> true
bool is_valid_email(const char* email, const char* domain);
//*You will implement this in subquestion 1*
//----------------------------------------------------------------------
// REQUIRES: Each line of input file "email.txt" is formatted:
//           <First Name><space><Last Name><space><email address><\n>
//           where <First Name>, <Last Name>, and <email address> are
//           all non-empty with no whitespace characters
// EFFECTS:  Writes email addresses with domain to output file "good.txt"
//           Each line of "good.txt" should be formatted:
//           <email><\n>
// EXAMPLES: Given "emails.txt" with contents below:

void split_emails(const string &domain);
//*You will implement this in subquestion (2)*

int main(int argc, char const *argv[])
{
    assert(is_valid_email("audladd@umich.edu", "umich") == true);
    cout << is_valid_email("audladd@umich.edu", "umich");
    split_emails("umich");

    return 0;
}

bool is_valid_email(const char* email, const char* domain){
    const char* domain_email = email;
    const char* temail = email;
    while(*temail != '@'){
        domain_email++;
        temail++;
    }
    domain_email++;
    while (*domain_email == *domain || *domain_email != '.')
        if (*domain_email != *domain)
            return false;
        else
            domain++, domain_email++;
    return true;
}

void split_emails(const string &domain){
ifstream fin;
fin.open("email.txt");
string fn, ln, email;
string filename = "good.txt";
ofstream fout;
fout.open(filename);
while(fin >>fn>>ln>>email){
    if(is_valid_email(email.c_str(), domain.c_str())){
        cout << fn << ln<< email;
        fout << email << endl;
    }
}
}