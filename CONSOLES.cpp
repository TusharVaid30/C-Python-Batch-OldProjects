#include <iostream> 
#include <conio.h> 
using namespace std; 
#include <windows.h> 
const int width = 120 , height = 40 ; 

int main() { 
    char *screen = new char[width*height] ; 
    HANDLE Console = CreateConsoleScreenBuffer( GENERIC_READ | GENERIC_WRITE , 0 , NULL , CONSOLE_TEXTMODE_BUFFER , NULL ) ; 
    SetConsoleActiveScreenBuffer(Console) ; 
    DWORD Bytes_written = 0 ;
    wstring map ; 
    while(!kbhit()) { 
        for(int x = 0 ; x < width ; x++ ) { 
            for( int y = 0 ; y < height ; y++ ) { 
                cout << 'x'  ; 
            }
        }
        screen[width*height - 1] = '\0' ;
        WriteConsoleOutputCharacter(Console , screen , width*height , { 0 , 0 } , &Bytes_written) ; 
    }
}
