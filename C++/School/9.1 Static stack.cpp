#include <iostream>
using namespace std ;
#define size_of_stack 5

class Static_Stack
{
    int A[size_of_stack] , Top ;

public :
    Array_Stack()
    {
        Top = - 1 ;
    }
    void push()
    {
        if( Top == size_of_stack - 1 ) 
            cout << "Overflow , Stack is full.\n" ;
        else
        {
            cout << "Enter element for index " << Top << " :>" ;
            cin  >> A[Top] ;
            Top ++ ;
        }
    }
    void pop ()
    {
        if( Top == -1 )
            cout << "Underflow , Stack is empty.\n" ;
        else
        {
            cout << "Removed element " << A[Top]      ; 
            cout << " from the index " << Top << endl ;
            Top -- ;
        }
    }
    void print()
    {
        if( Top == -1 ) 
            cout << "Stack is currently empty." ;
        else 
        {
            cout << "Stack in sequence :\n" ;
            for(int i = Top - 1 ; i >= 0 ; i--) cout << A[i] << " " ;
            cout << endl ;
        }
    }
};
            
int main()
{
    Static_Stack X ;
    int  C ;
    char R ;
    cout << "Created Static Stack.\n"   ;
    cout << "Maximum elements : " << size_of_stack << endl ;
    cout << "1 : Push into the Stack.\n" ;
    cout << "2 : Pop  from the Stack.\n" ;
    cout << "3 : Print Stack.\n"         ; 
    do{
        cout << "Enter Choice :> " ; cin >> C ;
        switch(C)
        {
            case 1 : X.push()  ; break ;
            case 2 : X.pop()   ; break ; 
            case 3 : X.print() ; break ;
            default: cout << "Invalid input." ;
        }
        cout << "Repeat again? ( Y/N ) :>" ; cin >> R ;
    }while( R == 'Y' ) ;
    return 1 ;
}
