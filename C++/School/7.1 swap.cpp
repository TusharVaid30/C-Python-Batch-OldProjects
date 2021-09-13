#include <iostream>
using namespace std ; 
#define Variable_Name( Variable ) # Variable

void Value_in(int &x , char* y)
{
    cout << "Enter Value of " << y << "\n>" ; cin >> x ;
}

void Value_of(int  x , char* y)
{
    cout << y << " = " << x << endl ;
}

int main()
{
    int A , B  ;
    Value_in(A , Variable_Name(A))  ;  Value_in(B , Variable_Name(B)) ;
    
    Value_of(A , Variable_Name(A))  ;  Value_of(B , Variable_Name(B)) ;
    
    int *pA = &A  , *pB = &B  , Temp       ;
    Temp    = *pA ; *pA = *pB ; *pB = Temp ;
    
    cout << "Swapped Values." << endl ;
    Value_of(A , Variable_Name(A))  ;  Value_of(B , Variable_Name(B)) ;

    delete pA , pB ;
    return 1       ;
}
