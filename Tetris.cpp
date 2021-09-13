#include <conio.h>    
#include <string.h>  
#include <stdlib.h>  
#include <iostream> 
#include <fstream>    
#include <windows.h> 
using namespace std ;

void gotoxy(int x , int y)
{
    static HANDLE h = NULL ;
    if(!h) h = GetStdHandle(STD_OUTPUT_HANDLE) ;
    COORD c = { x , y };
    SetConsoleCursorPosition(h,c) ;
}
int random( int AAA ) 
{
    return rand()%AAA ;
}

void cls()
{
     system("cls") ;
}

void CLS()
{
	 gotoxy(0,0) ; 
}

void spaceing(int Space_amount , char C = ' ' )
{
	 for(int i = 0 ; i < Space_amount ; i++) cout << C ;
}

int intlen(int Arg)
{
     int _ = 0 ; 
     do{ Arg /= 10 ; _ ++ ; }while( Arg > 0 ) ; 
     return _ ;
}

void framepause(long double _framepause_ = 20000)
{
	for(long double i = 0 ; i < _framepause_ ; i++)
	for(long double j = 0 ; j < _framepause_ ; j++) ; 
}

const int Length_Floor = 20 , Length_Wall = 30 ; 
int Taken_Points_Counter = 0 , Counts = 0 , Count_Count = 5  ; 
const 
char Up = 'w' , 
     Down = 's' ,
     Left = 'a' ,
     Right = 'd' , 
     Space = ' ' , 
     Floor = '-' , 
     Wall  = '|' ,
     Texture = '#' ; 
     struct Point
{
	int x , y ;
	char Char ;
	Point()
	{
		x = y = -1 ;
	}
	void Set( int X , int Y )
	{
		x = X ;
		y = Y ;
	}
} Taken_Points[Length_Floor*Length_Wall] ;

struct Block
{
    int Moving ; 
    Point A , B , C , D , *Arra[4] = { &A , &B , &C , &D }  ;
    Block()
    {
        Reset() ;
    }
    void Reset() 
    {
        Moving = 1 ; 
        int _ ; 
        for( _ = 0 ; _ < 4 ; _++ ) 
        {
            Arra[_]->Char = Texture ;
        }
        _ = random(2) ; 
        switch(_)
        {
            case 0 : // Square 
        A.Set(Length_Floor/2 ,0) ; B.Set(Length_Floor/2,1) ; C.Set(Length_Floor/2 + 1 ,0) ; D.Set(Length_Floor/2 + 1,1) ;
            break ;
            case 1 : //Line 
        A.Set(Length_Floor/2 ,0) ; B.Set(Length_Floor/2,1) ; C.Set(Length_Floor/2,2) ; D.Set(Length_Floor/2,3) ;
            break ; 
        }
        
    }
    void Move_Y( int DY )
    {
        for( int _ = 0 ; _ < 4 ; _++ ) 
        {
            Arra[_]->y += DY ;
        }
    }
    void Move_X( int DX )
    {
        for( int _ = 0 ; _ < 4 ; _++ ) 
        {
            Arra[_]->x += DX;
        }
    }
} Cube ;

char Current_Location_Point( int LOCATION_X , int LOCATION_Y)
{    
	int _ , __ ; 
    for( _ = 0 ; _ < 4 ; _++ ) 
    {
        if(Cube.Arra[_]->x == LOCATION_X and Cube.Arra[_]->y == LOCATION_Y) return Cube.Arra[_]->Char ; 
    }
    for( _ = 0 ; _ < Taken_Points_Counter ; _++ ) 
    {
        if(Taken_Points[_].x == LOCATION_X and Taken_Points[_].y == LOCATION_Y) return Texture ;
    }
    
    if( LOCATION_Y == Length_Wall ) return Floor ; 
    if( LOCATION_X == 1 or LOCATION_X == Length_Floor ) return Wall ; 
    return Space ; 
}


void Logic()
{
    int _ , __  , Must_Stop = 0 ; 
    for( _ = 0 ; _ < 4 ; _++ ) 
    {
        if( Cube.Arra[_]->y == Length_Wall - 1 ) Must_Stop = 1 ;
        for( __ = 0 ; __ < Taken_Points_Counter ; __++ ) 
        {
            if( Cube.Arra[_]->x == Taken_Points[__].x and Cube.Arra[_]->y == Taken_Points[__].y - 1 ) Must_Stop = 1 ;
        }
    }
    if( Must_Stop )
    {
        Cube.Moving = 0 ;
        for( _ = 0 ; _ < 4 ; _++ ) 
        {
            Taken_Points[ Taken_Points_Counter++ ].Set( Cube.Arra[_]->x , Cube.Arra[_]->y) ;
        }
        Cube.Reset() ; 
    }
    if( Cube.Moving && Counts%Count_Count == 0 ){ Counts = 0 ; Cube.Move_Y(1) ; } 
}

void Draw()
{
    CLS() ; 
    for( int _ = 1 ; _ <= Length_Wall ; _++ ) 
    {
        for( int __ = 1 ; __ <= Length_Floor ; __++ ) 
        {
            cout << Current_Location_Point( __ , _ ) ;  
        }
        cout << '\n' ;
    }
    framepause(5000) ;
}

void Controls()
{
    char In ; 
    int _ , __ = 1 ; 
    if(kbhit() ) 
    {
        In = getch() ; 
        switch(In) 
        {
            //case Up    : Cube.Move_Y(-1) ; break ;
            case Down  : for( _ = 0 ; _ < 4 ; _++ )
                         {
                              __ = 1 ; 
                         }
                         Cube.Move_Y( 1) ; break ; 
            case Left  : Cube.Move_X(-1) ; break ; 
            case Right : Cube.Move_X( 1) ; break ; 
        }
    }
}

        
int main() 
{
    char x = ' ' ;
    while(1) 
    {
        Draw();
        Logic() ; 
        Controls() ;
        Counts++ ; 
    }
    return 1 ; 
}

