#include <conio.h>    // Clear Screen And getch()
#include <string.h>   // Copy and Compare Strings
#include <stdlib.h>   // Random 
#include <iostream>   // Cout
#include <fstream>    // To handle Highscores 
#include <windows.h>
using namespace std ;

void spaceing(int Space_amount , char C = ' ' )
{
	 for(int _ = 0 ; _ < Space_amount ; _++) cout << C ;
}

int intlen(int i)
{
     int _ = 0 ; do{ i /= 10 ; _ ++ ; }while( i > 0 ) ; return _ ;
}

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
void cls()
{
     system("cls") ;
}
void CLS()
{
	 gotoxy(0,0) ; // system("cls") ;
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
        strcpy(Player_Name , "") ;
    }
    void Get(int e , int ge)
    {
        cout << "Enter Name :>" ;
        gets(Player_Name) ;
        Player_Score = e ;
        Player_Goodeats = ge ; 
    }
    void Put()
    {
        cout <<  Player_Rank ;
        if(Player_Rank < 10) cout << " " ;
        cout << " :  | " << Player_Name ;
        spaceing( 15 - strlen(Player_Name) , ' ' ) ;
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
    char* Name()
    {
        return Player_Name ;
    }
    
} PLAYERS[20] ;



struct Ability
{
    char Name[20] , Type[20] ; 
    void (*Execute)() ;
} A[11] ;

void Swap( int     &A , int     &B ){ int     Temp = A ; A = B ; B = Temp ; }
void Swap( Player  &A , Player  &B ){ Player  Temp = A ; A = B ; B = Temp ; }
void Swap( Ability &A , Ability &B ){ Ability Temp = A ; A = B ; B = Temp ; } 


const char    Apple = 'o' , 
			  Space = ' ' ,

			  Starting_Wall = 'X' ,
			  Special_Wall  = '#' ,  
			  Special_Tail  = '+' , 
			  Normal_Wall   = '.' , 
			  Normal_Tail   = ':' ,
			  
			  Up    = 'w' ,
			  Down  = 's' ,
			  Left  = 'a' ,
			  Right = 'd' ,
			  Power = ' ' ,
			  q     = 'q' , 

			  *POINTER       =   "\b\b:> "    ,
			  *Y_HARD_SPACE[]= 
									{  ""            ,
										"\n"         ,
										"\n\n"       ,
										"\n\n\n"     , 
										"\n\n\n\n"   , 
										"\n\n\n\n\n" ,
									}                ,
			  *MAIN_MENU_1[] =
									{
										"PLAY"       ,
										"HIGHSCORES" ,
										"HELP"   ,
                                        "CREDITS"    ,
										"QUIT"       ,
									}                , 
			  *MAIN_MENU_2[] =
									{
										"Play "       ,
										"Highscores " ,
										"Help "       ,
										"Credits "    ,
										"Quit "       ,
									}                ,
			  *BYE_SCREEN_1[]=
									{
										"I can play a litte more." ,
										"I have to go."            ,
									}                              ,
			  *BYE_SCREEN_2[]=
									{
										"YES                      ",
										"NO                       ",
									}        ,
               *Quote = "\"Either make something unique, or make nothing at all.\"" ,
               *File = "Ging gong.BAT" ;

const int     Max_Players      = 10   ,
              Restart_time     = 3    ,
              Hyper_Counts     = 5    , 
			  pause            = 3000 ,
			  XWALL            = 25   ,
			  YWALL            = 15   ,

			  XSPACEING        = 23   ,
			  YSPACEING        = 5    ,
				
			  OPTION_PLAY      = 0 ,
			  OPTION_HIGHSCORE = 1 ,
			  OPTION_HELP      = 2 ,
			  OPTION_CREDITS   = 3 , 
			  OPTION_QUIT      = 4 ,
			  OPTION_QUIT_YES  = 0 ,
			  OPTION_QUIT_NOPE = 1 ;
		
			  
char  Head  = '*' ,
	  Tail  = '+' ,
	  Wall  = Starting_Wall ,
	  dir ,
      Display[500] ; 

int   New_Scorer = -1 , Total_Players = 10 , LEGEND = -1 , Lowest_High , Lowest_Low , Lowest_Player ,
      x , y ,  ax , ay , Score , Eats , Good_Eats , Good_Eats_Per , body , Pause , Immortal , 
      Hyper_Mode = 1 , 
      Hide_Body , 
      Tripping ,
      Switching = 0 ,
      Switch_Value = 10 , 
      Switch_Hub ,
      Hyper_Count ,
      Previous_Score , 
      Zig_Zag , Zag_Zig , Zig_Value = 1 , Zag_Value = 3 , Zag_Value_Mod = 1 , 
      End = 0 , 
      epilepsy = 0 ,
      Active_Temp ,  
	  b  = 1 ,
	  s  = 100 , 
	  gs = 6*s ,
	  
	  xwall  = XWALL , 
	  ywall  = YWALL ,
	 
	  framecount  =   0 , 
	  framelag    =  30 , 
	  special_lag =   0 ,

	  xbody[150] , //XWALL*YWALL - 2*(XWALL + YWALL)] , 
	  ybody[150] , //XWALL*YWALL - 2*(XWALL + YWALL)] , 

	  Xspaceing_Menu = 46 , //XSPACEING ,
	  Yspaceing_Menu = 10 , //YSPACEING ,

      Xspaceing_Score= 30 ,
      Yspaceing_Score= 4  , 
	  Xspaceing_Game = XSPACEING ,
	  Yspaceing_Game = YSPACEING ,

	  Xspaceing_Over = XSPACEING ,
	  Yspaceing_Over = YSPACEING ,



	  Gameover , 
	  YTREWQ = 0 ,
	  MAIN_CURRENT = 0 ,
	  BYE_CURRENT = 0  ;							

void  Main_Menu() , 
      Game()      , 
	  Over()      ,
	  Draw()      ,
	  Bye()       ; 

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

void Show_Highscore()
{    
    CLS() ; 
    char* topper = "RANK         NAME         SCORE\n"  ;
    spaceing( Yspaceing_Score , '\n' ) ;
    spaceing( Xspaceing_Score ) ;
    cout << topper ;
    spaceing( Xspaceing_Score );
    spaceing( strlen(topper) , '_' ) ;
    cout << "\n" ;
    spaceing(50) ; 
    cout << "\n" ;  
    
    for(int Current_Player = 0 ; Current_Player < Total_Players ; Current_Player ++ ) 
    {
    // && Current_Player <= Max_Players)
        spaceing(Xspaceing_Score) ; 
        PLAYERS[Current_Player].Put() ;
        if( Current_Player == LEGEND ) cout << " < LEGEND " ;
        if( Current_Player >= Max_Players ) cout << " << Out !" ;
        if( Current_Player == New_Scorer ) cout << " < New !" ;
        spaceing(15) ; 
        cout << "\n" ;
    }
    spaceing( Xspaceing_Score ) ;
    spaceing( strlen(topper) , '_' ) ;
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
                Show_Highscore() ;
                framepause(8000) ; //getch() ;
            }
    }
    
}

void New_Highscore(int e , int gep)
{
    Total_Players += 1 ; 
    New_Scorer = Total_Players ;
    PLAYERS[New_Scorer].Get(e , gep) ;
    cls() ; 
}

void Write_Players()
{
    PLAYERS[0].Set_Info( New_Scorer ) ;
    PLAYERS[1].Set_Info( LEGEND ) ;
    ofstream F(File , ios :: binary | ios :: out ) ;
    for( int _ = 0 ; _ < Total_Players ; _++ )
        F.write((char*)&PLAYERS[_] , sizeof(PLAYERS[_])) ;
    F.close() ;
}

void Put_Apple(int NOT_X = -1 , int NOT_Y = -1)
{
	 ax = 3 + rand()%(xwall - 3) ;
	 ay = 3 + rand()%(ywall - 3) ;
	 if(ax == NOT_X && ay == NOT_Y ) Put_Apple(NOT_X,NOT_Y) ;
	 for(int _ = 0 ; _ < body ; _ ++ )
	 {
		  if(xbody[_] == ax && ybody[_] == ay) Put_Apple(NOT_X,NOT_Y) ;
	 }
}

void Put_Point( int &THIS_X , int &THIS_Y )
{
     THIS_X = 3 + rand()%(xwall - 3) ;
     THIS_Y = 3 + rand()%(ywall - 3) ;
}

void Walls_Modify( short A )
{
	xwall += A ; Xspaceing_Game -= A/2 ;
	ywall += A ; Yspaceing_Game -= A/2 ;
}

void Walls_Switch()
{
    if(framecount == framelag)
	 {
		  if(Wall == Normal_Wall)
		  {
				Wall = Special_Wall ;
				Tail = Special_Tail ;
				//framecount = special_lag ;
				if(Hyper_Count <= 1) 
                {
                     Hyper_Count = Hyper_Counts ; 
                     Switching = 1 ;
                 }
                else Hyper_Count -- ; 
		  }
		  else 
		  {
				Wall = Normal_Wall  ;
				Tail = Normal_Tail  ;
				//framecount = 0  ;
				if(Hyper_Count <= 1)
				{
                     Hyper_Count = Hyper_Counts ; 
                     Switching = 1 ;
                }
                else Hyper_Count --  ; 
		  }
	 }
	 if( framecount > framelag ) framecount = 0 ; 
}
void Epilepsy()
{
	if(Tripping&&epilepsy) if (xwall < XWALL + 8) Walls_Modify(2); else  Tripping = 0 ;
	else if(xwall > XWALL) Walls_Modify(-2); else Tripping = 1 ;
}

void Ability_Nothing(){}  

void Ability_Teleport()
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

void Ability_Reverse()
{
	x = xbody[body] ;
	y = ybody[body] ;
	if     (ybody[body-1] > ybody[body]) dir = 'u' ;  
	else if(ybody[body-1] < ybody[body]) dir = 'd' ;
	else if(xbody[body-1] > xbody[body]) dir = 'l' ;
	else if(xbody[body-1] < xbody[body]) dir = 'r' ;
	int _ , __ ;
	for(_ = 0 , __ = body ; _ <= body/2 ; _++ , __ --)
	{
		swap(xbody[_] , xbody[__]) ;
		swap(ybody[_] , ybody[__]) ;
	}
}

void Ability_Pause() { Pause == 1 ? Pause = 0 : Pause = 1 ; }

void Ability_Immortal() { Immortal = 1 ; }

 void Ability_Epilepsy() { epilepsy = 1 ; Tripping = 1 ;  }
    
 void Ability_Invisible() { Hide_Body = 1 ; } 
 
 void Ability_Feast()  { } 
 
 void Ability_Zigzag() { Zig_Zag = 1 ; }
 void Ability_Zagzig() { Zag_Zig = 1 ; } 
 void Fresh_Ability()
 {
      if(Zig_Zag || Zag_Zig) cls() ; 
      Zig_Zag = 0 ; 
      Zag_Zig = 0 ; 
      Immortal = 0 ;
      Hide_Body = 0 ;
      Hyper_Mode = 1 ; 
      if( ax > xwall || ay > ywall ) Put_Apple() ; 
      
  }
 void Null_Ability(Ability &Abi )
 {
     strcpy(Abi.Name,"            ") ; 
     strcpy(Abi.Type,"       ") ; 
     Abi.Execute = Ability_Nothing ; 
 }
 
 void Make_Ability(Ability &Abi) // 12 should be length of all bois 
 {
     int _ = rand()%50 ;
     if(_ >=  0 && _ < 10){ strcpy(Abi.Name , "Teleport    ") ; Abi.Execute = Ability_Teleport    ; }
     if(_ >= 10 && _ < 20){ strcpy(Abi.Name , "Reverse     ") ; Abi.Execute = Ability_Reverse     ; }
     if(_ >= 20 && _ < 30){ strcpy(Abi.Name , "Pause       ") ; Abi.Execute = Ability_Pause       ; }
     if(_ >= 30 && _ < 40){ strcpy(Abi.Name , "Immortality ") ; Abi.Execute = Ability_Immortal    ; }
     if(_ == 40) { strcpy(Abi.Name , "Eat Feast!! ") ; Abi.Execute = Ability_Feast     ; }
     if(_ == 41) { strcpy(Abi.Name , "Invisible!  ") ; Abi.Execute = Ability_Invisible ; }
     if(_ == 42) { strcpy(Abi.Name , "||Epilepsy||") ; Abi.Execute = Ability_Epilepsy  ; }
     if(_ == 43) { strcpy(Abi.Name , "ZIG ZAGGY ! ") ; Abi.Execute = Ability_Zigzag    ; } 
     if(_ == 44) { strcpy(Abi.Name , "ZAGGY ZIG ! ") ; Abi.Execute = Ability_Zagzig    ; } 
     if(  strcmp(Abi.Name , "Teleport    ") == 0 
     ||   strcmp(Abi.Name , "Reverse     ") == 0 
     ||   strcmp(Abi.Name , "Freeze      ") == 0 
     ||   strcmp(Abi.Name , "Pause       ") == 0 ) strcpy(Abi.Type , "Active ") ;
     else strcpy(Abi.Type , "Passive" ) ;  
     
 }
     
 void Switch_Ability()
 {
      switch(Switching)
      {
          case 1 : Null_Ability(A[0]) ; Fresh_Ability() ; // break ;
          case 2 : 
          case 3 :
          case 4 : Swap(A[Switching - 1] , A[Switching]) ; Switching += 1 ; break ;
      }
      if(Switching == 5) { Swap( A[Switch_Value] , A[Switch_Value - 1] ) ; Switch_Value -= 1 ; } 
      if(Switching == 5 && Switch_Value == 3) 
      { 
           Switch_Value = 10 ; Switching = 0 ; 
           Make_Ability(A[10]) ;
      }    
      if( strcmp(A[0].Type , "Passive" ) == 0 ) { A[0].Execute() ; A[0].Execute = Ability_Nothing ; }
      else Active_Temp = 4 ; 
}
           
int main()
{
     Read_Players() ; 
	 while(! End) Main_Menu() ; 
     return 1 ; 
}

void Back()
{
     char _  ;
	 cout << POINTER << "Return to Main Menu." ;
	 while(_ != Power) _ = getch() ;
	 cls() ; 
}

void Help()
{
     CLS() ; spaceing(5 , '\n') ; 
     char * Halp[] = { "Classic Nokia Snake game with added things!"                            ,
                       "Blank"                                                                  ,
                       "Abilites are self explainatory as per thier names."                     ,
                       "Of course , Active Abilities are to be activated by power button."      ,
                       "Passive ones are passive."                                              , 
                       "Blank"                                                                  ,
                       "Feel free to use them to your advantage!"                               ,
                       "Blank"                                                                  ,
                       "Good eats are the eats you eat while in HYPER MODE."                    , 
                       "These eats on HYPER MODE give 5 times more points than usual!"          ,
                       "HYPER MODE will activate harmonically , you'll know when that happens." , 
                       "Blank"                                                                  ,
                       "Blank"                                                                  ,
                       "Blank"                                                                  , }  ;   
     int _ = -1 , __ ;
     while(_++ < 13)
     { 
            spaceing(50 - strlen(Halp[_])/2) ; 
            for(__ = 0 ; __ < strlen(Halp[_]) ; __++)
                if(strcmp(Halp[_],"Blank") == 0){ spaceing(150) ; break ;} else cout << Halp[_][__] ; 
            cout << '\n' ; 
     } 
     spaceing(40) ;
     Back() ;
     cls() ; 
}
void Credits()
{
     cls() ;
     spaceing(3 , '\n' ) ;
     spaceing(45) ; cout << "GAME BY :\n" ;
     ifstream F("Chinmay_Header.txt" , ios :: in ) ;
     char _ ; 
     F.get(_) ;
     while( !F.eof()) 
     {
         cout << _ ;
         F.get(_) ;
     }
     F.close() ;
     spaceing(1 , '\n' ) ;
     spaceing(43) ; 
     cout << "CLASS : XII D\n" ;
     spaceing(43) ;
     cout << "BATCH : 2019-20\n" ; 
     spaceing(50 - strlen(Quote)/2) ; 
     cout << Quote << "\n\n" ;
     spaceing(40) ;
     Back() ; 
}
void Run_Game() 
{ 
     cls() ; 
	 Game() ; 
	 Fresh_Ability() ; 
	 int x = body ;  
	 for( int _ = 0 ; _ <= x ; _++)
	 {
			body-- ;
			Draw() ;
			framepause(pause) ;
	 }
	 Over() ;
}

void Main_Menu_Select(int SELECT)
{
	 switch(SELECT)
	 {
		  case OPTION_PLAY      : Run_Game() ; break ;
		  case OPTION_HIGHSCORE : Show_Highscore() ; cout << '\n' ; 
                                  spaceing(Xspaceing_Score + 5) ; Back() ; break ;
		  case OPTION_HELP      : Help()    ; break ;
		  case OPTION_CREDITS   : Credits() ; break ; 
		  case OPTION_QUIT      : cls() ; Bye() ; break ;
	 }
}

void Main_Menu()
{
	 CLS() ;
	 spaceing(Yspaceing_Menu , '\n' ) ; // 
	 for( int _ = OPTION_PLAY ; _ <= OPTION_QUIT ; _ ++ )
	 {
		  spaceing(Xspaceing_Menu) ; //SPACEING ;
		  if( MAIN_CURRENT == _ ) cout << POINTER << MAIN_MENU_1[_] << endl ;
		  else cout << MAIN_MENU_2[_] << endl ;
	 }
	 char x = getch() ;
	 switch(x)
	 {
		  case Up    : if( MAIN_CURRENT > OPTION_PLAY ) MAIN_CURRENT-- ; Main_Menu() ; break ;
		  case Down  : if( MAIN_CURRENT < OPTION_QUIT ) MAIN_CURRENT++ ; Main_Menu() ; break ;
		  case Power : Main_Menu_Select(MAIN_CURRENT) ; break ; 
	 }
}

void Bye_Select(int SELECT) 
{
     switch(SELECT)
     {
          case OPTION_QUIT_YES  : cls() ; Main_Menu() ; break ; 
          case OPTION_QUIT_NOPE : End = 1 ; 
                                  cls() ; 
                                  spaceing(10,'\n') ;
                                  spaceing(30) ;
                                  cout << "bye." ;
                                  break ;
     }
}
     
void Bye()
{
     CLS() ;
	 spaceing(Yspaceing_Menu , '\n' ) ; 
	 spaceing(Xspaceing_Menu - 10) ;
	 cout << "< Can't you play a little longer ?\n\n\n" ; 
	 for( int _ = 0 ; _ <= OPTION_QUIT_NOPE ; _ ++ )
	 {
		  spaceing(Xspaceing_Menu) ; 
		  if( BYE_CURRENT == _ ) cout << POINTER << BYE_SCREEN_1[_] << endl ;
		  else cout << BYE_SCREEN_2[_] << endl ;
	 }
	 char x = getch() ;
	 switch(x)
	 {
		  case Up    : if( BYE_CURRENT > OPTION_QUIT_YES  ) BYE_CURRENT-- ; Bye() ; break ;
		  case Down  : if( BYE_CURRENT < OPTION_QUIT_NOPE ) BYE_CURRENT++ ; Bye() ; break ;
		  case Power : Bye_Select(BYE_CURRENT) ; break ; 
	}
}
	
char Current_Location_Point( int LOCATION_X , int LOCATION_Y)
{
	 if(LOCATION_Y == 0  || LOCATION_Y == ywall) return Wall  ; 
	 if(LOCATION_X == 0  || LOCATION_X == xwall) return Wall  ; 
	 if(LOCATION_X == x  && LOCATION_Y == y    ) return Head  ; 
	 if(LOCATION_X == ax && LOCATION_Y  == ay  ) return Apple ; 
	 for(int _ = 0 ; _ <= body ; _++)
	 {
		  if(LOCATION_X == xbody[_] && LOCATION_Y  == ybody[_])
		  {
				if( ! Hide_Body ) return Tail ; 
		  }
	 }
	 return Space ; 
}

void Current_Location_Line_Pre( int LOCATION_Y ) 
{
    int _ = 0 , __ ; 
    static int ___ ;
    char Line[20] ; 
    switch(LOCATION_Y)
    {
        case 0 : _ = 1 ; strcpy(Line , "- Score -") ;  break ;
        case 1 : _ = 2 ; break ;
        case 3 : _ = 1 ; strcpy(Line , "- Good Eats -") ; break ; 
        case 4 : _ = 3 ; break ;
        case 9 : if(Score > PLAYERS[0].Score()){_ = 1 ; strcpy(Line , "TOP PLAYER BEATEN!") ;}break ; 
        case 10: if(Score < PLAYERS[0].Score()){_ = 1 ; strcpy(Line , "AIM FOR") ; }break ;
        case 11: _ = 4 ; break ;
        case 12: if(Score < PLAYERS[0].Score()){_ = 1 ; strcpy(Line , "TO BEAT PLAYER") ;}break ;
        case 13: if(Score < PLAYERS[0].Score()){_ = 1 ; strcpy(Line , PLAYERS[Lowest_Player].Name()) ;}break ;
    }
    // 1 is lines 2 is score 3 is goodeatsper 4 highgihg
    switch(_)
    {
        case 1 : spaceing(10 + strlen(Line)/2 , '\b') ; cout << Line ; 
                 spaceing(10 + strlen(Line)/2 - strlen(Line) ) ; break ;
        case 2 : __ = 1 ; if ( Score > Lowest_Low ) __++ ; if( Score > Lowest_High ) __ ++ ; 
                 spaceing(10 + 2 + __ + intlen(Score)/2 , '\b') ; 
                 spaceing(__ , ':') ;
                 cout << "> " << Score << " <" ;
                 spaceing(__ , ':') ; 
                 spaceing(10 - 2 - __ + intlen(Score)/2 - intlen(Score) ) ; break ;
        case 3 : //if(Previous_Score <= Score && ___ == 3 ) ___ = 0 ; // FLASH FLASH 
                 if (Good_Eats_Per < 70 && ___ > 1) ___ -- ; 
                 if (Good_Eats_Per == 100 && ___ < 3) ___++ ; 
                 if (Good_Eats_Per != 100 && ___ < 2 && Good_Eats_Per > 70) ___++ ; 
                 spaceing(10 + 3 + ___ + intlen(Good_Eats_Per)/2 , '\b') ;
                 spaceing(___ , '|') ; 
                 cout << ">  " << Good_Eats_Per << "% <" ;
                 spaceing(___ , '|') ;
                 spaceing(10 - 3 - ___ + intlen(Good_Eats_Per)/2 - intlen(Good_Eats_Per) ) ; break ;
        case 4 : if(Score < PLAYERS[0].Score())
                 {
                     spaceing(10 + 3 + intlen(Lowest_High)/2 , '\b') ; cout << "<  " << Lowest_High << "+ >" ;
                     spaceing(10 - 3 + intlen(Lowest_High)/2 - intlen(Lowest_High) ) ; break ;
                 }
                 break ;
     }
}

void Current_Location_Line_Post( int LOCATION_Y )
{
     switch(LOCATION_Y)
     {
         case 0  : cout << "\bX==:> " ;
                   if(Switching) cout << "Switching Ability!" ; 
                   else cout << "Next Ability in " << Hyper_Count << "." ; break ; 
         case 2  : cout << " :> Current Ability " ; 
                   spaceing(4 - framecount%2) ;
                   cout << POINTER ; 
                   spaceing(framecount%2) ; 
                   cout << A[0].Name ; break ;
         case 3  : cout << " :> Ability Type " ;
                   if(strcmp(A[0].Type,"Active ")==0)
                   {spaceing(4  - Active_Temp,'-');spaceing(Active_Temp);if(Active_Temp > 0)Active_Temp--;}
                   else spaceing(3) ;
                   cout << ":> " << A[0].Type ; break ;
         case 6  : cout << " Coming Up Next "   ; 
                   if(Hyper_Count == 1){ spaceing(framecount%4 ,'!') ; spaceing(4 - framecount%4)  ; }
                   else cout << "!     " ;
                   break ; 
         case 7  : cout << "||>  " ; break  ;
         case 8  : cout << "|>  "  ; break  ;
         case 9  : cout << ">  "   ; break  ;
     }
     if(LOCATION_Y > 6 && LOCATION_Y < 16) cout << A[LOCATION_Y - 6].Name ;
}
 
void Header()
{
      //spaceing(Yspaceing_Game , '\n') ;
	 spaceing(Xspaceing_Game )       ;
	 if(Gameover)  cout << "<GAME OVER>" ;
	 spaceing(xwall , ' ') ;
	 if(Wall == Special_Wall) { Gameover ? spaceing(17 , '\b') : 
     spaceing(6 + framecount%(xwall - 6) , '\b') ; cout << "<HYPER> " ; }
	 else spaceing(20) ; 
	 cout << '\n' ;
}

void Tailer()
{
     if(Score > Lowest_Low)
     {
         cout << "\n" ;
         spaceing(Xspaceing_Game + xwall/2 - 7 - strlen(PLAYERS[Lowest_Player+1].Name())/2) ;
         cout << "You've beaten " << PLAYERS[Lowest_Player+1].Name() << " !              \n" ;
         spaceing(Xspaceing_Game + xwall/2 - 8) ; 
         if(Lowest_Player == 0) cout << "\bTop Position" ;
         else cout << "Position " << Lowest_Player + 2 ;
         cout << " Secured.  \n" ;
     }
 }
void Setup()
{    Tripping = 0 ; 
     Lowest_Player = 9 ;
     Lowest_High = Lowest_Low = PLAYERS[Lowest_Player].Score() ; 
     int _ = -1 ; while(_++ <= 10) Null_Ability(A[_]) ; 
     Hyper_Count = Hyper_Counts ; 
     Wall = Starting_Wall ; 
	 Put_Point(x,y) ; 
	 dir   = ' ' ;
	 for(int _ = 0 ; _ < body ; _ ++){xbody[_] = -1 ;ybody[_] = -1 ;}
	 body  = 1   ;
	 Eats  = Good_Eats = Good_Eats_Per = Score = 0 ;
	 Put_Apple(x,y) ;
	 Switch_Hub = Gameover = 0  ;
     Fresh_Ability() ; 	 
}
    
void Draw()
{
	 CLS() ; 
	 cout << Y_HARD_SPACE[Yspaceing_Game] ;
	 Header() ; 
	 for(unsigned short _ = 0 ; _ <= ywall ; _ ++)
	 {
		  spaceing(Xspaceing_Game) ; 
		  if( ! Gameover ) Current_Location_Line_Pre(_) ; 
		  if( (_%2 == 0) && Zig_Zag ) spaceing(Zig_Value) ;
		  if( (_%2 == 0) && Zag_Zig ) spaceing(Zag_Value) ; 
		  if( (_%2 != 0) && Zag_Zig ) spaceing(3 - Zag_Value) ; 
		  for(unsigned short __ = 0 ; __ <= xwall ; __++)
		  {
				cout << Current_Location_Point( __ , _ ) ;
		  }
		  if( ! Gameover ) Current_Location_Line_Post(_) ; 
		  cout << '\n' ; 
	 }
	 if( ! Gameover ) Tailer() ; 
	 framecount += 1 ;
	 framepause(pause) ;
}

void Move()
{
	 switch(dir)
	 {
		  case 'u' : Head = '^' ; y-- ; break; 
		  case 'd' : Head = 'v' ; y++ ; break; 
		  case 'l' : Head = '<' ; x-- ; break; 
		  case 'r' : Head = '>' ; x++ ; break; 
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
				case Power : A[0].Execute() ; break ;
				case q     : Gameover = 1 ;
		  }
	 }
}

void Logic()
{
	 int _ ;
	 int prevX = xbody[0] , prev2X;
	 int prevY = ybody[0] , prev2Y;
	 xbody[0]  = x ; ybody[0] = y ;
	 for(_ = 1 ; _ <= body ; _++)
	 {
		  prev2X = xbody[_]; xbody[_] = prevX ;
		  prev2Y = ybody[_]; ybody[_] = prevY ;  
		  prevX  = prev2X  ;
		  prevY  = prev2Y  ; 
	 }
	 if(!Immortal)
		  for( _ = 2 ; _ < body ; _++)
				if(x == xbody[_] && y == ybody[_]){ cls() ; Wall = ' ' ;  Gameover = 1; }
	 if (x == ax && y == ay)
	 {  
		 body  += b ;
		 Previous_Score = Score ; 
		 if(Wall == Normal_Wall) Score += s ;
		 else {  Good_Eats++ ; Score += gs ;  }
		 Eats  ++ ; 
		 Good_Eats_Per = 100*Good_Eats/Eats ;
		 Put_Apple(x,y);
	 }
	 if ((x > xwall - 1 ) && (dir == 'r')) x = 1         ;
	 if ((x < 1)          && (dir == 'l')) x = xwall - 1 ;    
	 if ((y > ywall - 1 ) && (dir == 'd')) y = 1         ;
	 if ((y < 1)          && (dir == 'u')) y = ywall - 1 ; 
	 Epilepsy() ;
	 if(Tripping&&!( xwall > XWALL )&&epilepsy&&(strcmp(A[0].Name , "||Epilepsy||") != 0)) 
     { cls() ; Tripping = 0 ; epilepsy = 0 ;} 
     if (Hyper_Mode) Walls_Switch() ; 	
     if (Switching) Switch_Ability() ;
     if (Switch_Hub == 0){ Make_Ability(A[10]) ; Switching = 4 ; Switch_Hub++ ; }
     //if (Switch_Hub == 1){ Hyper_Count = 0  ; Switch_Hub++ ; }
     if (Switch_Hub == 1 && ! Switching ) { Make_Ability(A[10]) ; Switching = 3 ; Switch_Hub++ ; } 
     if (Switch_Hub == 2 && ! Switching ) { Make_Ability(A[10]) ; Switching = 2 ; Switch_Hub++ ; } 
     if (Switch_Hub == 3 && ! Switching ) { Make_Ability(A[10]) ; Switching = 1 ; Switch_Hub++ ; }  
     
     //if (Switch_Hub == 4 && ! Switching ) { for(int _ = 4;_<10;_++)Null_Ability(A[_]) ; Switch_Hub = -1 ; } 
     if (Score > Lowest_High && Lowest_Player > 0) 
     {
          Lowest_Player-- ; 
          Lowest_High = PLAYERS[Lowest_Player].Score() ;
     }
     if(Zag_Zig)
     {
          if((Zag_Value == 0 && Zag_Value_Mod == -1)||(Zag_Value == 3 && Zag_Value_Mod == 1)) Zag_Value_Mod *= -1 ; 
         Zag_Value += Zag_Value_Mod ;
 }
}
void Game()
{
	 Setup();
	 while(!Gameover)
	 {
		  Draw();
		  Input();
		  if(!Pause){ Move() ; Logic() ; }
	 }
}

void Over()
{
	 cls() ;
	 spaceing(Yspaceing_Over , '\n' ) ;
	 spaceing(Xspaceing_Over )        ; 
	 cout << "Game Over\n"    ;
	 spaceing(Xspaceing_Over) ;
	 if(Score > Lowest_Low) 
     {
          cout << "New Highscore!\n\n" ;
          spaceing(Xspaceing_Over) ;
          New_Highscore(Score , Good_Eats_Per) ;
          Player_Sort(PLAYERS , Total_Players + 1) ; 
          Write_Players() ;
          cout << "\n\n" ; 
          spaceing(Xspaceing_Score + 5) ; 
      }
     else 
     {
     cout << "Better Luck Next Time!\n" ; 
	 spaceing(Xspaceing_Over) ;
	 cout << "Eats        : " << Eats << '\n' ;
	 spaceing(Xspaceing_Over) ;
	 cout << "Good eats   : " << Good_Eats     ; 
	 Good_Eats_Per == 100 ? cout << "(100%)" : cout << "(" << Good_Eats_Per << "%)" ; 
	 cout << '\n' ;
	 spaceing(Xspaceing_Over) ;
	 cout << "Final Score : " << Score << "\n\n" ;
     spaceing(Xspaceing_Over) ;  
     }
     Back() ; 
}
