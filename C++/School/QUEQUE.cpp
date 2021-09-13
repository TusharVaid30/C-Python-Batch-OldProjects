#include <iostream>
using namespace std ;

class Static_Linear_Queue
{
    int A[max_size] , front , rear ;

public :
    Static_Queue()
    {
        front = rear = -1 ;
    }
    void Insert()
    {
        if( rear == max_size - 1 )
            cout << "Overflow, Queue is full.\n" ;
        else if( rear == -1 )
        {
            front = rear = 0 ;
            cout << "Enter value for Index " << rear << "\n>" ;
            cin  >> A[rear]  ;
        }
        else 
        {
            rear++           ;
            cout << "Enter value for Index " << rear << "\n>" ;
            cin  >> A[rear]  ;
        }
    }
    void Remove()
    {
        if( front == -1 )
            cout << "Underflow, Queue is empty.\n" ;
        else if( front == rear )
        {
            cout << "Removed element " << A[rear]  << " from index " ;
            cout << rear << "\nThe Queue is now empty." << endl      ;
            front = rear = -1 ;
        }
        else 
        {
            cout << "Removed element " << A[rear]  << " from index " ;
            cout << rear << "\nThe Queue has "     << rear - front   ;
            cout << " elements left." << endl ;
            rear -- ;
        }
    }
    void Print()
    {
        if( front == rear )
            cout << "Queue is empty." ;
            
