#include <iostream>
using namespace std;

class Top{
public:
    void f1(){
        cout << "f1_top" << endl;
    }
    
    virtual void f2(){
        cout << "f2_top" << endl;
    }
};

class Mid : public Top{
public:
    void f1(){
        cout << "f1_mid" << endl;
    }
    
    virtual void f2(){
        cout << "f2_mid" << endl;
    }
};

class Bottom : public Mid{
public:
    void f1(){
        cout << "f1_bot" << endl;
    }
    
    virtual void f2(){
        cout << "f2_bot" << endl;
    }
};

int main(int argc, char const *argv[])
{
    Top top;
    Mid mid;
    Bottom bot;
    Top *t_ptr = &top;
    Top *t_ptr2 = &mid;
    Top *t_ptr3 = &bot;
    Mid *m_ptr = &bot;

    cout << "top.f1();" << endl;
    top.f1();
    cout << endl;
    cout << "top.f2();" << endl;
    top.f2();
    cout << endl;
    cout << "mid.f1();" << endl;
    mid.f1();
    cout << endl;
    cout << "mid.f2();" << endl;
    mid.f2();
    cout << endl;
    cout << "t_ptr->f1();" << endl;
    t_ptr->f1();
    cout << endl;
    cout << "t_ptr->f2();" << endl;
    t_ptr->f2();
    cout << endl;
    cout << "t_ptr2->f1();" << endl;
    t_ptr2->f1();
    cout << endl;
    cout << "t_ptr2->f2();" << endl;
    t_ptr2->f2();
    cout << endl;
    cout << "m_ptr->f1();" << endl;
    m_ptr->f1();
    cout << endl;
    cout << "m_ptr->f2();" << endl;
    m_ptr->f2();
    cout << endl;
    cout << "t_ptr3->f1();" << endl;
    t_ptr3->f1();
    cout << endl;
    cout << "t_ptr3->f2();" << endl;
    t_ptr3->f2();
    


    return 0;
}
