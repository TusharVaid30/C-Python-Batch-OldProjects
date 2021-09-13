#include <iostream> 
#include <math.h>
using namespace std ; 
#include <windows.h> 
int width = 120 , height = 40 ; 
float player_x = 8 , player_y = 8 , player_a = 0 ; 
float map_width = 16 , map_height = 16 ; 
float fov = 3.14/4 ; 
float depth = 16 ;

int main() 
{
    wchar_t *screen = new wchar_t[width*height] ; 
    HANDLE Console = CreateConsoleScreenBuffer( GENERIC_READ | GENERIC_WRITE , 0 , NULL , CONSOLE_TEXTMODE_BUFFER , NULL ) ; 
    SetConsoleActiveScreenBuffer(Console) ; 
    DWORD Bytes_written = 0 ;
    wstring map ; 
    map += L"################" ; 
    map += L"#..............#" ;
    map += L"#..........#####" ;
    map += L"#..............#" ;
    map += L"#..............#" ;
    map += L"########.......#" ;
    map += L"#......#.......#" ;
    map += L"#..P...........#" ;
    map += L"#......#.......#" ;
    map += L"########.......#" ;
    map += L"#..............#" ;
    map += L"#..............#" ;
    map += L"#.......#......#" ;
    map += L"#.......#......#" ;
    map += L"#.......#......#" ;
    map += L"################" ;
    while(1) 
    { 
        for( int x = 0 ; x < width ; x++ ) 
        { 
            float ray_a = (player_a - fov/2.0f) + ((float)x/(float)width)*fov ; 
            float dist = 0 ; 
            bool hit_wall = false ; 
            float eye_x = sin(ray_a) ; 
            float eye_y = cos(ray_a) ; 
            while( !hit_wall && dist < depth ) 
            { 
                dist += 0.1f ; 
                int test_x = (int)(player_x + eye_x*dist) ; 
                int test_y = (int)(player_y + eye_y*dist) ; 
                if( test_x < 0 || test_x > map_width || test_y < 0 || test_y > map_height) 
                { 
                    hit_wall = true ; 
                    dist = depth ; 
                } 
                else 
                { 
                    if( map[test_y + map_width*test_x] == '#' ) 
                    {
                        hit_wall = true ;  
                    }
                }
            }
            int ceiling = (float)(height/2.0) - height/((float)dist) ; 
            int floor = height - ceiling ; 
            for(int y = 0 ; y < height ; y++ )
            {
                char c ; 
                if( y < ceiling ) c = ' ' ; 
                else if( y > ceiling && y < floor ) c = '#' ; 
                else c = ' ' ; 
                screen[y*width + x] = c ;
            }
        }
        screen[width*height - 1] = '\0' ;
        WriteConsoleOutputCharacter(Console , (const char*)screen , width*height , { 0 , 0 } , &Bytes_written) ; 
    }
    return 0 ;
}
