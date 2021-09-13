#include <conio.h>  
#include <stdlib.h>   
#include <iostream>   
#include <windows.h> 
using namespace std ; 

#define Max_Stars 80*26 

void framepause(long double _framepause_)
{
	for(long double i = 0 ; i < _framepause_ ; i++)
	for(long double j = 0 ; j < _framepause_ ; j++) ; 
}

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

const int Stars_Floor = 25 , Stars_Roof = -500 , Stars_L_wall = 0 , Stars_R_wall = 80 ;

struct Point
{
	int x , y , Moving ;
	char Char ;
	Point()
	{
		x = y = 0 ;
		Moving = 0 ;
	}
	void Set( int X , int Y )
	{
		x = X ;
		y = Y ;
	}

} Stars[Max_Stars] ;

void Go( Point P , char C )
{
	if( P.x > 0 && P.y > 0 && P.x < 80 && P.y < 26 )
	{
		gotoxy( P.x  , P.y ) ;
		cout << C ;
	}
}

void Move_Stars()
{
    int Loop_1 , Loop_2 , wind ;
    wind = random(3) ; 
    for( Loop_1 = 0 ; Loop_1 < Max_Stars ; Loop_1++ )
    {
         if(!Stars[Loop_1].Moving){ continue ; }
         Go(Stars[Loop_1] , ' ') ;
         Stars[Loop_1].x -= 0 ; //1 + random(2) + wind ;
         Stars[Loop_1].y -= -1 ; // random(2) + random(2) + 1 ;
	     //if( Stars[Loop_1].y < Stars_Roof   ) Stars[Loop_1].y = Stars_Floor  ;
	     if( Stars[Loop_1].y == Stars_Floor  ) 
         {
              //Stars[Loop_1].y = Stars_Roof   ;
              //Stars[Loop_1].x = random(Stars_R_wall - Stars_L_wall) + Stars_L_wall ; 
              
              Stars[Loop_1].Moving = 0 ; 
         }
	     if( Stars[Loop_1].x < Stars_L_wall ) Stars[Loop_1].x = Stars_R_wall ;
	     if( Stars[Loop_1].x > Stars_R_wall ) Stars[Loop_1].x = Stars_L_wall ;
	     for( Loop_2 = 0 ; Loop_2 < Max_Stars ; Loop_2 ++ )
         {
              if(Stars[Loop_1].y == Stars[Loop_2].y - 1 
              && Stars[Loop_1].x == Stars[Loop_2].x
              && !Stars[Loop_2].Moving  ) 
              {
                   Stars[Loop_1].Moving = 0 ;
                   //if(Stars[Loop_2].Char == '.') Stars[Loop_2].Char = '*' ; 
                   
                   
                   Go(Stars[Loop_2] , Stars[Loop_2].Char ) ;
                   break ;
              }
         }
         Go(Stars[Loop_1] , Stars[Loop_1].Char ) ;
    }
    framepause(1500) ;
}

void Refresh()
{
    for( int i = 0 ; i < Max_Stars ; i++ )
	{
		if( Stars[i].Moving ) continue ;
        Go(Stars[i ] , ' ') ;
        Stars[i].Set( random(Stars_R_wall - Stars_L_wall) + Stars_L_wall ,
			          random(Stars_Floor  -  Stars_Roof ) + Stars_Roof   ) ;
		if( i%15 == 0 ) Stars[i].Char = '*' ;
		else if( i%50 == 0 ) Stars[i].Char = 'X' ; 
		else Stars[i].Char = '.' ; 
		Stars[i].Moving = 1 ; 
	}
}


int main()
{
		
    char x = 'x' ; 	
            			      //80 and 25
	Refresh() ; 
    while(1)
    {
         Move_Stars() ;
         if( kbhit() ) x = getch() ;
         if( x == ' ') 
         {
             Refresh() ;  
             x = 'x' ;
         }
     }
	return 1 ;
}












