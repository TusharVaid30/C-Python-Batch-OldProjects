#include <windows.h>
#include <conio.h>  
#include <iostream> 
#include <math.h> 
using namespace std ;

void gotoxy(int x , int y)
{
    static HANDLE h = NULL ;
    if(!h) h = GetStdHandle(STD_OUTPUT_HANDLE) ;
    COORD c = { x , y };
    SetConsoleCursorPosition(h,c) ;
}
float pi = 3.1415926535897932384626433832795028 ; 
float theter = 0 ; 
void circle( int x , int y , float r , char c , float w = 4 , bool out = false ) { 
    for( float theta = 0 ; theta < theter ; theta += 0.03 ) {    
        for( float o = r - w ; o <= r + w ; o += 0.5 ) { 
            gotoxy( cos(theta)*o*1.5 + x , sin(theta)*o + y ) ; 
            if( out and (o == r-w or o == r+w) ) cout << 'x' ; 
            else cout << c ;   
        }
    }
} // YO WHJAT THE FUCK ARE EXPONENTS ? 1.1 POWER OF NEGATIVES WHA THE FUYCK FUCK WHAT IS 0.1 FUCK WHAT ?

int main() { 
    float x = 45 , y = 20 , Percent = 0 ; 
    char c ; 
    while( 1 ) {
        theter = pi*(Percent/50) ; 
        gotoxy( x - Percent/100 , y ) ; 
        cout << Percent << "%" ; 
        if( Percent < 100 ) { 
            circle( x , y , 14 , '#' , 4 ,  true ) ;
            gotoxy( x - 3, y - 2 ) ; 
            cout << "Loading" ;
        }
        else {  
            gotoxy( x - 4 , y + 2 ) ; 
            cout << "Finished!" ; 
            break ; 
        }
        if( Percent == 99 ) {  gotoxy( x - 3 , y - 2 ) ; cout << "       " ; }
        if( Percent < 100 ) Percent++ ; 
    }    
    theter = 2.5*pi ; 
    circle( x , y , 14 , '#' , 4 , true ) ; 
    theter = 0 ; 
    while( theter <= 2.5*pi ) { 
        circle( x , y , 14 , '$' , 1 ) ; 
        theter += 0.3 ; 
    } 
    gotoxy( x - 13 , y - 2 ) ; 
    cout << "Press any key to continue." ; 
    getch() ; 
    return 1 ; 
}         
