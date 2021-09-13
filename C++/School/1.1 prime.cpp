#include <iostream>
using namespace std ;

char prime( int N )
{
    char is_prime = 't' ;
    if(N == 1) is_prime = 'f' ;
    for(int  i = 2 ; i <= N/2 ; i++)
    {
        if(N%i == 0)
        {
            is_prime = 'f' ;
            break   ;
        }
    }
    return is_prime ;
}

int main()
{
    int  primes = 0 , x = 1 ;
    char is_a_prime ;
    while(primes <= 20)
    {
        is_a_prime = prime(x) ;
        if(is_a_prime == 't')
        { 
            cout << x << endl ;
            primes ++         ;
        }
        x ++ ;
    }
               
    return 0 ;
}
