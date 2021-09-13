#include <iostream>
using namespace std ;

struct Node 
{
    int   Data ;
    Node *Next ;
} ;

class Dynamic_Queue
{
    Node *Rear , *Front ;
public :
    Dynamic_Queue()
    {
        Front = Rear = NULL ; 
    }
    
    void Insert()
    {
        Node *Temp = new Node   ; 
        cout << "Enter Data :>" ;
        cin  >> Temp -> Data ;
        Temp -> Next =  NULL ; 
        if( Front == NULL )
        {
            Front = Rear = Temp ;
        }
        else 
        {
            Rear -> Next = Temp ;
            Rear = Temp ;
        }
    }
    
    void Remove()
    {
        if( Front == NULL )
        {
            cout << "Queue is empty.\n" ;
            return ; 
        } 
        Node *Temp = Front ;
        cout << "Deleted Value :" ;
        cout <<  Temp -> Data  ;  
        if( Front == Rear )
        {
            Front  = Rear = NULL  ; 
        }
        else
        {
            Front = Front -> Next ;
        }
        delete Temp ; 
    }
    
    void Display() 
    {
        if( Front == NULL )
        {
            cout << "Queue is empty.\n" ;
            return ;
        }
        Node  *Temp  = Front ;
        cout << "Front : \n" ;
        while( Temp != NULL )
        {
            cout << "Data  :-  " ;
            cout << Temp -> Data ;
            Temp  = Temp -> Next ;
            cout << endl ;
        }
        cout << "^Rear." ;
    }
    
    ~Dynamic_Queue()
    {
        while( Front != NULL )
        {
            Node  *Temp   = Front ;
            Front = Front -> Next ;
            delete Temp ;
        }
    }
} ;

int main()
{
    Dynamic_Queue X ;
    cout << "Created a Dynamic Queue. \n" ;
    cout << " 1 : Insert into Queue." << endl ;
    cout << " 2 : Remove from Queue." << endl ;
    cout << " 3 : Print  the  Queue." << endl ;
    char Repeat ; int Switchs ;
    do{
        cout << "Enter Option :>" ; 
        cin  >> Switchs ;
        switch(Switchs)
        {
            case 1 :  X.Insert()  ; break ;
            case 2 :  X.Remove()  ; break ;
            case 3 :  X.Display() ; break ; 
            default: cout << "Invalid Input." ;
        }
        cout << "\n Repeat again? ( Y/N ) :>" ; 
        cin  >> Repeat ;
    }while( Repeat == 'Y' ) ;
    return 1 ;
}
