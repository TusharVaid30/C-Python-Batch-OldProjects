#include <conio.h>
#include <unistd.h>
#include <stdlib.h>
#include <iostream>     
using namespace std ;
void cls(){system("cls");}//cout << "\x1b[2J";}

const char apple = 155 ,
           space = ' ' ,
           special_wall = '#' , // 177 , 
           special_tail = '+' , // 158 , 
           normal_wall  = '.' , // 176 ,
           normal_tail  = ':' ,
           
           Up    = 'w' ,
           Down  = 's' ,
           Left  = 'a' ,
           Right = 'd' ,
           Power = ' ' ,
           q     = 'q' ;
           
char head  = '*' ,
     tail  = '+' ,
     wall  = 158 ; //'+' ;
char dir;
const int Restart_time = 3 , pause = 30000 ,
          xwall = 25 , ywall = 10 ; //MAX 117 , 27 IN DEFAULT BUFFER 2K
int x , y ,  ax , ay , Score , eats , goodeats , s = 1 , gs = 6 ,
    xbody[xwall*ywall - 2*(xwall + ywall)] , framecount = 0 , framelag = 30  , special_lag = 0 ,
    ybody[xwall*ywall - 2*(xwall + ywall)] , body   , b = 1 ;


float  goodeats_per ;
string spaceing(int Space_amount , char C)
{
    string S = "" ;
    for(int _ = 0 ; _ < Space_amount ; _++)
    {
        S += C ;
    }
    return S ;
}
    
const char 
*Xspaceing = "\t\t\t     "   ,
*Yspaceing = "\n\n\n\n\n\n\n" ;

string     
Display                         ,
XSPACEING  = Xspaceing + spaceing(xwall/2 - 5 , ' ') ,
YSPACEING  = Yspaceing + spaceing(ywall/2   , '\n' ) ;

void 
Game()  , Over()     ,
Draw()  , Input()    , Logic()   ,
Setup() , putapple() , Ability() ; 
bool Gameover ;

int MAIN_CURRENT = 0 ;
const char* POINTER = "\b\b\b:> " ;

char* MAIN_MENU[]=
{
    "Play"       ,
    "Highscores" ,
    "Controls"   ,
    "Quit"       ,
} ;

const int 
OPTION_PLAY      = 0 ,
OPTION_HIGHSCORE = 1 ,
OPTION_CONTROLS  = 2 ,
OPTION_QUIT      = 3 ;
//
//MAIN_MENU[OPTION_PLAY]       = "Play"       ;
//MAIN_MENU[OPTION_HIGHSCORES] = "Highscores" ;
//MAIN_MENU[OPTION_CONTROLS]   = "Controls"   ;
//MAIN_MENU[OPTION_QUIT]       = "Quit"       ;
// 

void RUN_GAME() 
{
    Game() ; sleep(1) ; 
    Over() ;
}
    
void MAIN_MENU_SELECT(int SELECT)
{
    switch(SELECT)
    {
        case OPTION_PLAY      : RUN_GAME() ; break ;
        case OPTION_HIGHSCORE : break ;
        case OPTION_CONTROLS  : break ;
        case OPTION_QUIT      : exit(1) ; break ;
    }
}
    
void MAIN()
{
    cls() ;
    cout << YSPACEING ;
    for( int _ = OPTION_PLAY ; _ <= OPTION_QUIT ; _ ++ )
    {
        cout << XSPACEING ;
        if( MAIN_CURRENT == _ ) cout << POINTER ;
        cout << MAIN_MENU[_] << '\n' ;
    }
    char x = getch() ;
    switch(x)
    {
        case Up    : if( MAIN_CURRENT > OPTION_PLAY ) MAIN_CURRENT-- ; break ;
        case Down  : if( MAIN_CURRENT < OPTION_QUIT ) MAIN_CURRENT++ ; break ;
        case Power : MAIN_MENU_SELECT(MAIN_CURRENT) ; break ; 
    }
}
int main()
{
    
    while(1) MAIN() ;
    return 1 ;
}












void putapple(int NOT_X , int NOT_Y)
{
    ax = 1 + rand()%(xwall-1) ;
    ay = 1 + rand()%(ywall-1) ;
    if(ax == NOT_X && ay == NOT_Y ) putapple(NOT_X,NOT_Y) ;
    for(int _ = 0 ; _ < body ; _ ++ )
    {
        if(xbody[_] == ax && ybody[_] == ay) putapple(NOT_X,NOT_Y) ;
    }
}
void Setup()
{
    x = 1 + rand()%(xwall-1) ;
    y = 1 + rand()%(ywall-1) ;
    dir   = ' ' ;
    head  = '*' ,
    Score = 0   ;
    for(int _ = 0 ; _ < body ; _ ++)
    {
        xbody[_] = -1 ;
        ybody[_] = -1 ;
    }
    body  = 1   ;
    eats  = 0   ;
    body  = 1   ;
    eats  = 0   ; goodeats = 0  ; goodeats_per = 0 ;
    putapple(x,y) ;
    Gameover = false ;
    
}

void Draw()
{
    Display = "" ;
    Display += Yspaceing ;
    for(unsigned short _ = 0 ; _ <= ywall ; _ ++)
    {
        Display += Xspaceing ;
        for(unsigned short __ = 0 ; __ <= xwall ; __++)
        {
            
            if     (_  == 0  || _  == ywall) Display += wall ;
            else if(__ == 0  || __ == xwall) Display += wall ;
            else if(__ == x  && _  == y    ) Display += head ;
            else if(__ == ax && _  == ay   ) Display += apple;
            else 
            {       
                bool Tail_print = false;
                for(int ___ = 0 ; ___ <= body ; ___++)
                {
                    if(__ == xbody[___] && _  == ybody[___]    )
                    {
                       Display += tail ;
                       Tail_print = true ;
                    }
                }
                if(!Tail_print) Display += space ;
            }
        }
        Display += '\n' ;
    }
    Display += XSPACEING ;
    Display += "\b\b\b\b\b\b\b" ;
    Display += "Score :" ;
    Score > 99 ? Display += (unsigned short)Score/100 + 48 : Display += " " ;
    Score >  9 ? Display += (unsigned short)Score/10  + 48 : Display += " " ;
    Display += (unsigned short)Score%10 + 48 ;
    Display += "  Goodeats : " ;
    if(goodeats_per == 100) 
    {
        Display += "100%\n"  ;
        Display += Xspaceing ;  
        Display += "\t <Perfect>" ;
    }
    else
    {
        Display += (unsigned short)goodeats_per/10 + 48 ;
        Display += (unsigned short)goodeats_per%10 + 48 ;
        Display += "%" ;
    }
    usleep(pause) ;
    if(framecount == framelag)
    {
        framecount = 0 ;
        if(wall == normal_wall)
        {
            wall = special_wall ;
            tail = special_tail ;
            framecount = special_lag ;
        }
        else 
        {
            wall = normal_wall  ;
            tail = normal_tail  ;
            framecount = 0  ;
        }
    }
    framecount += 1 ;
    cls() ;
    cout << Display ;
//    cout << "Score : " << Score << "\tGEP : " << goodeats_per  << "%" ;
}
void Ability()
{
    if( !(xbody[body] > 0 && xbody[body] < xwall) ) return ;
    if( !(ybody[body] > 0 && ybody[body] < ywall) ) return ;
    x = xbody[body] ;
    y = ybody[body] ;
    if     (ybody[body-1] > ybody[body]) dir = 'u' ;  
    else if(ybody[body-1] < ybody[body]) dir = 'd' ;
    else if(xbody[body-1] > xbody[body]) dir = 'l' ;
    else if(xbody[body-1] < xbody[body]) dir = 'r' ;
    
}
void Move()
{
    switch(dir)
    {
        case 'u' : head = '^' ; y-- ; break; 
        case 'd' : head = 'v' ; y++ ; break; 
        case 'l' : head = '<' ; x-- ; break; 
        case 'r' : head = '>' ; x++ ; break; 
    }
//    if     (head == 'X') head = 'O' ;
//    else if(head == 'O') head = 'X' ;
//    if     (tail == 'x') tail = 'o' ;
//    else if(tail == 'o') tail = 'x' ;
}
void Input()
{
    if(kbhit())
    {
        switch(getch())
        {
            case Up    : if(dir != 'd') dir = 'u' ; break ;
            case Down  : if(dir != 'u') dir = 'd' ; break ;
            case Left  : if(dir != 'r') dir = 'l' ; break ;
            case Right : if(dir != 'l') dir = 'r' ; break ;
            case Power : Ability() ; break ;
            case q     : Gameover = true ;
        }
    }
}
void Logic()
{
    int prevX = xbody[0] , prev2X;
    int prevY = ybody[0] , prev2Y;
    xbody[0]  = x ; ybody[0] = y ;
    for(unsigned short _ = 1 ; _ <= body ; _++)
    {
        prev2X = xbody[_]; xbody[_] = prevX ;
        prev2Y = ybody[_]; ybody[_] = prevY ;  
        prevX  = prev2X  ;
        prevY  = prev2Y  ; 
    }
    for(int _ = 2 ; _ < body ; _++)
        if(x == xbody[_] && y == ybody[_]) Gameover = true;
    if (x == ax && y == ay)
    {  
       body  += b ;
       if(wall == normal_wall) Score += s ;
       else {  goodeats++ ; Score += gs ;  }
       eats  ++ ; 
       goodeats_per = 100*goodeats/eats ;
       putapple(x,y);
    }
    if ((x > xwall - 1 ) && (dir == 'r')) x = 1         ;
    if ((x < 1)          && (dir == 'l')) x = xwall - 1 ;    
    if ((y > ywall - 1 ) && (dir == 'd')) y = 1         ;
    if ((y < 1)          && (dir == 'u')) y = ywall - 1 ;    
}  
void Game()
{
    Setup();
    while(!Gameover)
    {
        Draw();
        Input();
        Move();
        Logic();
    }
}
void Over()
{
    Display  = "" ; Display += YSPACEING     ;
    Display += XSPACEING + "Game Over"       ;
    Display += '\n' ;
    
    Display += XSPACEING + "Eats        : "  ;
    Display += (unsigned short)eats/10 + 48  ;
    Display += (unsigned short)eats%10 + 48  ;
    Display += '\n' ;
    
    Display += XSPACEING + "Good eats   : "  ;
    Display += (unsigned short)goodeats/10 + 48  ; 
    Display += (unsigned short)goodeats%10 + 48  ;
    if(goodeats_per == 100) Display += "(100%)" ;
    else
    {
        Display += "(" ;
        Display += (unsigned short)goodeats_per/10 + 48 ;
        Display += (unsigned short)goodeats_per%10 + 48 ;
        Display += "%" ;
        Display += ")" ;
    }
    
    
    Display += '\n' ;
    
    Display += XSPACEING + "Final Score : "  ;
    Display += (unsigned short)Score/10 + 48 ;
    Display += (unsigned short)Score%10 + 48 ;
    Display += '\n' ;
    Display += '\n' ;
    
    cls() ;
    cout << Display ;
    char __________ ;
    int  _____ = 0  ;
    cout << XSPACEING << POINTER << "Retrun to Main Menu." ;
    while(__________ != Power) 
    {
        __________ = getch() ;
    }
//    for( int _ = Restart_time ; _ > 0 ; _-- )
//    {
//        cout << "\r" ;
//        cout << XSPACEING << "Restarting in " << _ << "." ;
//        sleep(1) ;
//    }
}
