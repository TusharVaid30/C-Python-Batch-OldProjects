#include <iostream>
#include <conio.h>

using namespace std ; 

int main()
{
    char x[20] ;
    cout << "Enter password :> " ; 
    for( int i = 0 ; i < 20 ; ) 
    {
        x[i] = getch() ;
        if(x[i] == 13) break ;
        if(x[i] == '\b') 
        {
            if( i <= 0 ) continue ; 
            cout << "\b \b" ;
            i-- ;
        }
        else 
        {
            cout << '*' ;
            i++ ;
        }
    }
    cout << endl << "Password was : " << x << endl ;  
    while(!kbhit()) cout << " \b" ; 
    return 1 ;
}
