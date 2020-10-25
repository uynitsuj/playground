#include <cassert>
#include <iostream>
using namespace std;

class Base {
    public:
        int x;
    protected:
        int y;
    private:
        int z;
};

class PublicDerived: public Base {
    // x is public
    // y is protected
    // z is not accessible from PublicDerived
};

class ProtectedDerived: protected Base {
    // x is protected
    // y is protected
    // z is not accessible from ProtectedDerived
};

class PrivateDerived: private Base {
    // x is private
    // y is private
    // z is not accessible from PrivateDerived
};

class Based{
public:
    static const int x = 0;
};

int main(int argc, char const *argv[])
{
    cout << Based::x;
    int a = 2;
    int g = *(&a);
    cout << g << endl;
    return 0;
}
