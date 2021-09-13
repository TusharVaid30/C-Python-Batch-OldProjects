#include <conio.h>
#include <stdio.h>
#include <stdlib.h>
#include <iostream>
using namespace std ;

const char Up    = 'w' ,
           Down  = 's' ,
           Left  = 'a' ,
           Right = 'd' ,
           i     = 'e' ;
char s ; 
void function1(){cout << "\nhi"    ; s = getch() ; } 
void function2(){cout << "\nhello" ; s = getch() ; } 
void function3(){cout << "\nSup"   ; s = getch() ; } 
void function4(){cout << "\nyo"    ; s = getch() ; } 
void menudriving() ;
int  menudriven () ;
int  current = 0   ;
const int max_menu = 4 ;   
char* A[max_menu] = { "Function 1" , "Function 2" , "Function 3" , "Function 4" } ;
void ACTUALMENU() 
{          
    for(int _ = 0 ; _ < 4 ; _++ ) 
    {
        cout << "\n\t\t\t" ;
        if(_ == current) cout << "\b\b\b:> " ;
        cout << A[_] ;
    }
}
void Function( int FID )
{
    switch(FID)
    {
        case 1 : function1() ; break ;
        case 2 : function2() ; break ;
        case 3 : function3() ; break ;
        case 4 : function4() ; break ;
    }
}
int main()
{
    char x ; 
    while(1)
    {
        ACTUALMENU() ;
        x = getch() ;
        switch(x)
        {
            case Up   : if(current > 0  ) current-- ; break ;
            case Down : if(current < max_menu - 1) current++ ; break ;
            case i    : Function(current + 1 ) ;
        }
        system("cls") ;
    }
    return 1 ;
}


void menudriving()
{
    int x = 1;
    while(x)
    {
        x = menudriven() ;
    }
}
    
int menudriven()
{
    int c ;
    for(int _ = 1 ; _ <= 4 ; _ ++) cout << "\n\t\t" << _ << " : FUNCTION " << _ ;
    cout << "\n\t\tINPUT CHOICE :>" ;
    cin  >> c ;
    
    switch(c)
    {
        case 1 : function1() ; break ;
        case 2 : function2() ; break ;
        case 3 : function3() ; break ;
        case 4 : function4() ; break ;
        default: cout << "bye" ; return 0 ;
    }
    return 1 ;
}
