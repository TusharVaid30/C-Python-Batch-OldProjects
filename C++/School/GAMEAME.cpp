#include <conio.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>
using namespace std ;

const int  Xwall = 15 ,
           Ywall = 15 ;

const char Space = ' ' ,
           Sta   = '*' ,
           Wall  = 'X' ;

string Display ;

struct Star
{
    int X = 3 ; //Xwall/2 ;
    int Y = 5 ; //Ywall/2 ;
} S ;

void MoveStar()
{
    S.X += rand()%(3) - 1 ;
    S.Y += rand()%(2) ;
    if      ( S.X >= Xwall ) S.X = 0     ;
    else if ( S.X <= 0     ) S.X = Xwall ;
    else if ( S.Y >= Ywall ) S.Y = 0     ;
    else if ( S.Y <= 0     ) S.Y = Ywall ; 
}

void Draw()
{
    Display = ""  ;
    
    for(int _ = 0 ; _ < Ywall ; _++)
    {
        for(int __ = 0 ; __ < Xwall ; __++)
        {
            if     ( _  == 0   || _  == Ywall - 1 ) Display += Wall ;
            else if( __ == 0   || __ == Xwall - 1 ) Display += Wall ; 
            else if( _  == S.Y && __ == S.X       ) Display += Sta  ;
            else Display += Space ;
        }
        Display += '\n' ;
    }
    system("cls")   ;
    cout << Display ;
}
    
int main()
{
    while( 1 ) { Draw()  ; MoveStar() ; }
    return 1 ;
}
