#include <iostream> 
using namespace std ; 

class student 
{
    int c[10] ; 
    float d ; 
    char t[10] ; 
} ; 

int main() 
{
    student s ; 
    cout << sizeof( student ) << endl ; 
    cout << sizeof( s ) << endl ; 
    return 0 ; 
} 
