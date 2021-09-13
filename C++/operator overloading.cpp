#include <iostream>

using namespace std ;


struct A 
{
    int x , y ;
    A(int X , int Y)
    {
        x = X ; 
        y = Y ;
    } 
    A()
    {
        x = y = 0 ;
    }
    void Show()
    {
        cout << x << '\t' << y << endl ;
    }
} ; 

A operator + ( A one , A two )
{
    A three ;
    three.x = one.x + two.x ;
    three.y = one.y + two.y ;
    return three ;
}

int main()
{
    A a(10 , 20) , b(30 , 40) , c ; 
    a.Show() ; 
    b.Show() ; 
    c = a + b ; 
    c.Show() ; 
    return 1 ;
}
