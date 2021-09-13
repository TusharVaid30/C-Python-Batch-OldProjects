#include <iostream>
#include <stdlib.h>
#include <stdio.h>
#include <conio.h>
#include <windows.h>
using namespace std ;

struct Point 
{
    int x , y ; 
    char Char ;
} ; 

void framepause(long double ___ = 20000)
{
	for(long double _  = 0 ; _ <___ ;  _++)
	for(long double __ = 0 ; __<___ ; __++) ; 
}

void gotoxy(int x , int y)
{
    static HANDLE h = NULL ;
    if(!h) h = GetStdHandle(STD_OUTPUT_HANDLE) ;
    COORD c = { x , y };
    SetConsoleCursorPosition(h,c) ;
}

void Go(Point P , char C = ' ')
{
    gotoxy(P.x - 1 , P.y) ;  
    cout << C ; 
}

int main()
{
    const int Number = 10 ; 
    Point A[Number] ; 
    const int Top = 0 , Bottom = 30 , Left = 0 , Right = 120 ; 
    for( int _ = 0 ; _ < Number ; _++) 
    {
        A[_].y = Top  + rand()%(Bottom - Top) ; 
        A[_].x = Left + rand()%(Right - Left) ;
        A[_].Char = '*' ; 
    }

    while(!kbhit())
    {
        for( int _ = 0 ; _ < Number ; _++ )
        {
            Go(A[_], ' ') ;
            A[_].x -= 1 ; 
            A[_].y -= 1 ; 
            Go(A[_] , (char) 48 + _) ;
            if( A[_].y < Top    ) A[_].y = Bottom ;
            if( A[_].y > Bottom ) A[_].y = Top    ; 
            if( A[_].x < Left   ) A[_].x = Right  ;
            if( A[_].x > Right  ) A[_].x = Left   ;
            framepause(100) ; 
        }
        framepause(2000) ; 
    } 
    
    return 1 ;
}
