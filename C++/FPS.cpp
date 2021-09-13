#include <iostream>
using namespace std;
#include <windows.h>

const int ScreenWidth = 120 , ScreenHeight = 40;
float PlayerX = 0.0 , PlayerY = 0.0 , PlayerA = 0.0 ;
float FOV = 3.14159265358979323846264338327950/4;
int MapHeight = 16 , MapWidth = 16 ;

int main()
{
    wchar_t *screen = new wchar_t[ScreenWidth*ScreenHeight];
    HANDLE Console = CreateConsoleScreenBuffer(GENERIC_READ |
    GENERIC_WRITE, 0, NULL, CONSOLE_TEXTMODE_BUFFER, NULL);
    SetConsoleActiveScreenBuffer(Console);
    DWORD BytesWritten = 0;
    wstring map;
    map += L"################";
    map += L"#              #";
    map += L"#              #";
    map += L"#              #";
    map += L"#              #"; 
    map += L"#              #";
    map += L"#              #";
    map += L"#              #";
    map += L"#              #";
    map += L"#              #";
    map += L"#              #";
    map += L"#              #";
    map += L"#              #";
    map += L"#              #";
    map += L"#              #";
    map += L"################";
    
    while(1)
    {
        for(int i = 0, i < ScreenWidth, i++)
        {
            float RayAngle = (Player - FOV/2.0)
                            +((float)i/(float)ScreenWidth)
                            *FOV ;
            float DistanceToWall = 0;
            bool  HitWall = false ;
            float EyeX = sinf(RayAngle);
            float EyeY = cosf(RayAngle);
            while(!HitWall)//11:10
        }
        screen[ScreenWidth*ScreenHeight - 1] = '\0';
        WriteConsoleOutputCharacter(Console, screen,
        ScreenWidth*ScreenHeight, {0,0}, &BytesWritten);
    }
    return 0;
}
