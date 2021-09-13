#include <fstream>
#include <string.h>
#include <iostream>
#include <conio.h> 
#include <unistd.h>
using namespace std ;
void cls() { system("cls") ; } 
const int Max_Players = 10 ;

char *File = "Guess htis" ;


int Total_Players = 0 , Xspaceing = 15 , Yspaceing = 3 , New_Scorer = -1 , 
    LEGEND = -1 ;

void Spaceing( int SS , char C = ' ' )
{
    for( int _ = 0 ; _ < SS ; _ ++ )
    {
        cout << C ;
    }
} 

class Player 
{
    int  Player_Score    , 
         Player_Goodeats ,
         Player_Rank     ,
         Player_Info     ;
    char Player_Name[10] ;

public :
    Player()
    {
        Player_Rank  = 0 ;
        Player_Score = 0 ;
        Player_Info  = 0 ;
        Player_Goodeats = 0 ;
        strcpy(Player_Name , "<unassigned>") ;
    }
    void Get()
    {
        static int x = 697000 ;
        Player_Score = x++ ;
        Spaceing( Yspaceing , '\n' ) ;
        Spaceing( Xspaceing ) ;
        cout << "Score : " << Player_Score << "\n" ;
        Spaceing( Xspaceing ) ;
        cout << "Enter Name  " << ":>" ;
        char Temp_Name[10] ;
        gets(Temp_Name) ;
        strcpy(Player_Name , Temp_Name) ;
    }
    void Put()
    {
        Spaceing( Xspaceing , ' ' ) ;
        cout <<  Player_Rank ;
        if(Player_Rank < 10) cout << " " ;
        cout << " :  | " << Player_Name ;
        Spaceing( 15 - strlen(Player_Name) , ' ' ) ;
        cout << "|  " ;
        if(Player_Score < 10) cout << " " ;
        cout << Player_Score << " (" << Player_Goodeats << "%)" ;
    } 
    void Set_Rank( int Rank )
    {
        Player_Rank = Rank ;
    }
    void Set_Info( int Info )
    {
        Player_Info = Info ;
    }
    int Score()
    {
        return Player_Score ;
    }
    int Info()
    {
        return Player_Info ;
    }
    
} ;

Player PLAYERS[20] ;

void Swap( Player &A , Player &B )
{
    Player Temp = A ; A = B ; B = Temp ;
}

void Read_Players()
{
    ifstream F(File , ios :: in | ios :: binary ) ;
    Player P  ;
    int Current_Player = 0 ;
    
    F.read((char*)&P , sizeof(P)) ;
    while(!F.eof() && Current_Player < Max_Players) 
    {
        PLAYERS[Current_Player ++] = P ;
        F.read((char*)&P , sizeof(P)) ;
    }
    Total_Players = Current_Player ;
    F.close() ;
    
    if(PLAYERS[0].Info() != 0 && Total_Players > 0 ) New_Scorer = PLAYERS[0].Info() ;
    if(PLAYERS[1].Info() != 0 && Total_Players > 1 ) LEGEND = PLAYERS[1].Info() ;
    if( LEGEND > Max_Players ) LEGEND = -1 ;
}

void SHOW_HIGHSCORE()
{    
    cls() ; 
    char* topper = "RANK        NAME        SCORE\n"  ;
    Spaceing( Yspaceing , '\n' ) ;
    Spaceing( Xspaceing ) ;
    cout << topper ;
    Spaceing( Xspaceing );
    Spaceing( strlen(topper) , '_' ) ;
    cout << "\n\n" ; 
    
    for(int Current_Player = 0 ; Current_Player < Total_Players ; Current_Player ++ ) 
    {
    // && Current_Player <= Max_Players)
    
        PLAYERS[Current_Player].Put() ;
        if( Current_Player == LEGEND ) cout << " < LEGEND " ;
        if( Current_Player >= Max_Players ) cout << " << Out !" ;
        if( Current_Player == New_Scorer ) cout << " < New !" ;
        cout << "\n" ;
    }
    Spaceing( Xspaceing ) ;
    Spaceing( strlen(topper) , '_' ) ;
    cout << "\n" ;    
}

        
void Player_Sort( Player A[] , int n )
{
    int Flag = 1 ;
    for( int a = 0 ; a < n - 1 ; a ++ )
    {
        Flag = 0 ;
        for( int b = 0 ; b < n - 1 - a ; b ++ )
            if( A[b].Score() < A[b + 1].Score() )
            {
                if( b + 1  == New_Scorer ) New_Scorer -- ; 
                if( b + 1  == LEGEND ) LEGEND -- ; 
                else if( b == LEGEND ) LEGEND ++ ; 
                
                Swap(A[b] , A[b+1]) ;
                Flag = 1 ;
                for( int c = 0 ; c <= Total_Players ; c++ )
                    PLAYERS[c].Set_Rank(c + 1) ;
                SHOW_HIGHSCORE() ;
                sleep(0) ;//getch() ;
                
            }
    }
    
}

void NEW_HIGHSCORE()
{
    PLAYERS[++Total_Players].Get() ;
    New_Scorer = Total_Players ;
}

void Write_Down()
{
    PLAYERS[0].Set_Info( New_Scorer ) ;
    PLAYERS[1].Set_Info( LEGEND ) ;
    ofstream F(File , ios :: binary | ios :: out ) ;
    for( int _ = 0 ; _ < Total_Players ; _++ )
        F.write((char*)&PLAYERS[_] , sizeof(PLAYERS[_])) ;
    F.close() ;
}

int main()
{
    Read_Players() ;
    int x = 0 ;
    while( x++ < 10 ){ NEW_HIGHSCORE() ; 
                      Player_Sort( PLAYERS , Total_Players + 1 ) ; 
                      SHOW_HIGHSCORE() ; }
                      
                      
    Write_Down() ; 
    return 1 ;
}
