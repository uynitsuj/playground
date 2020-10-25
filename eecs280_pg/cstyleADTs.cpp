#include <iostream>
#include <cassert>
using namespace std;
struct Triangle{
    double a;
    double b;
    double c;
};

void Triangle_init(Triangle *tri, double a_in, double b_in, double c_in);
double Triangle_perimeter(const Triangle *tri);
void Triangle_scale(Triangle *tri, double s);


int main(int argc, char const *argv[])
{
    Triangle t = {1, 2, 3};
    assert(Triangle_perimeter(&t) == 6);
    cout<<Triangle_perimeter(&t);
    Triangle d;
    Triangle_init(&d, 2,2,2);
    assert(Triangle_perimeter(&d) == 6);
    cout<<Triangle_perimeter(&d);
    Triangle_scale(&d, 2);
    assert(Triangle_perimeter(&d) == 12);
    cout<<Triangle_perimeter(&d);
    return 0;
}

void Triangle_init(Triangle  *tri, double a_in, double b_in, double c_in){
    tri->a = a_in;
    tri->b = b_in;
    tri->c = c_in;
}

// REQUIRES: tri points to a valid Triangle
// EFFECTS:  Returns the perimeter of the given Triangle.
double Triangle_perimeter(const Triangle *tri) {
  return tri->a + tri->b + tri->c;
}


// REQUIRES: tri points to a valid Triangle; s > 0
// MODIFIES: *tri
// EFFECTS:  Scales the sides of the Triangle by the factor s.
void Triangle_scale(Triangle *tri, double s){
    assert(s>0);
    tri->a*=s;
    tri->b*=s;
    tri->c*=s;
}