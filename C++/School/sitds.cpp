#include <iostream>
using namespace std ;

int main()
{
    char* S = "SHAKTI" ;
    int * p , v[] = { 10 , 15 , 70 , 19 } ;
    p = v ;
    cout << *p << S << endl ;
    S++ ; p ++ ;
    cout << *p << S << endl ;
    return 1 ;
}
