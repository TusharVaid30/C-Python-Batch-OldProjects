#include <iostream>
using namespace std ;

long Square( int x ) { return x*x   ; }
long Cube  ( int x ) { return x*x*x ; }

void Print_Array( int A[] , int Length )
{
    cout << "\nArray is { " << A[0] ;
    for(int i = 1 ; i < Length ; i++) cout << " , " << A[i] ;
    cout << " } ." << endl ; 
}

int main()
{
    int A[] = { 1 , 2 , 4 , 7 , 9 } , *p = A ;
    Print_Array(A , 5) ;
    for(int i = 0 ; i < 5 ; i++ , p++)
         if( *p % 2 == 1 )
              cout << "\nCube   of " << *p << " is " << Cube(*p)   ;
         else cout << "\nSquare of " << *p << " is " << Square(*p) ;

    return 1 ;
}
