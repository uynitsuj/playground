#include <iostream>
#include <Eigen/Dense>
 
using Eigen::MatrixXd; 
using namespace Eigen;
using namespace std;
 
int main()
{
    //Construct a 2x2 matrix using MatrixXd - d for double
    MatrixXd m(2,2);
    m(0,0) = 3;
    m(1,0) = 2.5;
    m(0,1) = -1;
    m(1,1) = m(1,0) + m(0,1);
    std::cout << m << std::endl;
    
    //Initialize a 3-by-3 matrix m2 using the Random() method 
    //with random values between -1 and 1
    MatrixXd m2 = MatrixXd::Random(3,3);
    
    //function call MatrixXd::Constant(3,3,1.2) returns a 3-by-3 
    //matrix expression having all coefficients equal to 1.2
    m2 = (m2 + MatrixXd::Constant(3,3,1.2)) * 50;

    cout << "m2 =" << endl << m2 << endl;

    //VectorXd is a (column) vector of constructor-defined size
    VectorXd v(3);
    v << 1, 2, 3;
    cout << "m2 * v =" << endl << m2 * v << endl;
}
