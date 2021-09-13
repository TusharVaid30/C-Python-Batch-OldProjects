#include <iostream>
using namespace std ;

class Distance
{
    int   feet   ;
    float inches ;
    
 public :
  
    void  set(int A , float B)
    {
        feet   = A  ;
        inches = B  ; 
        while( inches >= 12 )
        {
            feet   +=  1 ; 
            inches -= 12 ;
        }
    }
    void  disp()
    {
        cout << feet << " Feet, " << inches << " Inches." ;
        cout << endl  ;
    } 
    Distance add(Distance A )
    {
        Distance B ;
        B.set(A.feet+feet , A.inches+inches) ; 
        return B   ;
    }
};

int main()
{
    Distance X , Y , Z ;
    int      Feet_temp ;
    float    Inch_temp ;
    cout << "Input Distance 1\n"                  ;  
    cout << "Enter Feet   :>" ;  cin >> Feet_temp ;
    cout << "Enter Inches :>" ;  cin >> Inch_temp ;
    X.set(Feet_temp,Inch_temp);
    cout << "Input Distance 2\n"                  ;  
    cout << "Enter Feet   :>" ;  cin >> Feet_temp ;
    cout << "Enter Inches :>" ;  cin >> Inch_temp ;
    Y.set(Feet_temp,Inch_temp);
    Z = X.add(Y) ;
    cout << "-Distance 1 : " ;
    X.disp();
    cout << "-Distance 2 : " ;
    Y.disp();
    cout << "-Distance 3 : " ;
    Z.disp();
    return 0     ;
}
