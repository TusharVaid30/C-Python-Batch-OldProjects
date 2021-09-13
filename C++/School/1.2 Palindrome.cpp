#include <string.h>
#include <iostream>
using namespace std ;

char palindrome( char S[] )
{
    int  length = strlen(S) - 1 ;
    char is_pal = 'y' ;
    int  i = 0        ;
    int  j = length   ;
    
    for(  ; i < length/2 ; i ++ , j--)
    {
        if(S[i] != S[j])
        {
            is_pal = 'n' ;
            break ;
        }
    }
    return is_pal ;
}

int main()
{
    char s[20] ;
    cout << "Enter the String :>" ; gets(s);
    char is_a_pal = palindrome(s) ;
    
    if(is_a_pal == 'y')
          cout << "It is a Palindrome."    ;
    else 
          cout << "It isn't a Palindrome." ;
    return 0 ;
}
