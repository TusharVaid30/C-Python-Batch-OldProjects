#include <string.h>
#include <iostream>

using namespace std ;

int Palindrome(char* A)
{
    int i ; 
    char *p1 = A , *p2 = A ; 
    
    for( i = 0 ; i < strlen(A) - 1 ; i ++ ) p2 ++ ;
    for( i = 0 ; i < strlen(A)/2   ; i ++ ) 
    {
        if( *p1 != *p2 ) return 0 ;
        p1 ++ ;
        p2 -- ;
    }
    return 1 ;
}

int main()
{
    char C[20] ;
    cout << "Enter String :>" ; cin >> C ;
    cout << C << " is" ;
    if( ! Palindrome(C) ) cout << " not" ;
    cout << " a Palindrome."  ;
    
    return 1 ;
}
