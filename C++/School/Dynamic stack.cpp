#include <iostream>
using namespace std ; 
struct Node
{
    int   Data ;
    Node *Next ;
} ;

class Dynamic_Stack
{
    Node *Top ;     
public :
    Dynamic_Stack()
    {
        Top = NULL ;
    }
    void Push()
    {
        Node *Temp   = new Node ; 
        Temp -> Next = NULL     ;
        cout << "Enter Data :>" ;
        cin  >> Temp -> Data    ;
        if( Top == NULL ) 
        {
            Top = Temp ;
        }
        else 
        {
            Temp -> Next = Top  ;
            Top = Temp ;
        }
    }
    
    
    void Pop()
    {
        if( Top == NULL )
        {
            cout << "Stack is empty." ;
        }
        else 
        {
            cout << "Deleted value :" ;
            cout << Top -> Data ; 
            Node *Temp  =  Top  ;
            Top  =  Top -> Next ;
            delete Temp  ;
        }
    }
    

    void Print()
    {
        Node *Temp = Top  ;
        cout << "Top:>\n" ;
        while( Temp != NULL )
        {
            cout << "Data : " << Temp -> Data << endl ;
            Temp = Temp -> Next ;
        }
    }
    
    

    ~Dynamic_Stack()
    {
        while( Top != NULL )
        {
            Node *Temp = Top    ;
            Top  = Top -> Next  ;
            delete Temp ; 
        }
    }
} ;
int main()
{
    Dynamic_Stack X ;
    cout << "Created Dynamic Stack.\n" ;
    cout << " 1 : Push into Stack." << endl ;
    cout << " 2 : Pop  from Stack." << endl ;
    cout << " 3 : Print the Stack." << endl ;
    char Repeat ; int Switchs ;
    do{
        cout << "Enter Option :>" ; 
        cin  >> Switchs ;
        switch(Switchs)
        {
            case 1 : X.Push()  ; break ;
            case 2 : X.Pop()   ; break ;
            case 3 : X.Print() ; break ; 
            default: cout << "Invalid Input." ;
        }
        cout << "\n Repeat again? ( Y/N ) :>" ; 
        cin  >> Repeat ;
    }while( Repeat == 'Y' ) ;
    return 1 ;
}

