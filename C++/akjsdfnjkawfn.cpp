#include <conio.h>
#include <unistd.h>
#include <iostream>
using namespace std ;



void loop( char* Message , int times , int pause = 0 , int end = 0)
{
    for(unsigned short _ = 0 ; _ < times ; _++)
    {
        cout << Message << endl;
        sleep(pause) ;
    }
    sleep(end) ;
}



int main()
{
    loop(" WRITE 1",10,0,1) ; 
    clrscr();  
    loop(" Write 2",5,0,0) ;
    return 1 ;
}





//
//void recur(int x , int y = 0)
//{
//    cout << y << endl ;
//    if( y == x - 1 )
//        return ;
//    else 
//        recur(x,y+1) ;
//}
//int main() 
//{
//    int x = 10 ;
//    recur(x) ;
//    return 1 ;
//}
