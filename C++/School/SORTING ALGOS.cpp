#include <iostream>
using namespace std ;

typedef void (*Functions)(int* , int) ;

void Swap( int &A , int &B )
{
    int temp = A ; A = B ; B = temp ;
}

void Print( int A[] , int n , char space = ' ' )
{
    for( int _ = 0 ; _ < n ; _++ )
    {
        cout << A[_] << space ;
    }
    cout << endl ;
}


void Bubble_Sort( int A[] , int n )
{
    int flag = 1 ;
    
    for( int a = 0 ; a < n - 1 ; a ++ )
    {
        flag = 0 ;
        for( int b = 0 ; b < n - 1 - a ; b ++ )
        {
            if( A[b] > A[b + 1] )
            {
                flag = 1 ;
                Swap( A[b] , A[b + 1] ) ; 
            }
        }
    }
}

void Selection_Sort( int A[] , int n )
{
    int Smallest ;
   
    for( int a = 0 ; a < n - 1 ; a ++ )
    {
        Smallest = a ;        
        for( int b = a + 1 ; b < n ; b ++ )
        {
            if( A[Smallest] > A[b] )
            {
                Smallest = b ;
            }
        }
        Swap( A[Smallest] , A[a] ) ;
    }
}
        
void Insertion_Sort( int A[] , int n )
{
    for( int a = 1 ; a < n ; a ++ )
    {
        while( a > 0 )
        {
            if( A[a - 1] > A[a] )
            {
                Swap( A[a - 1] , A[a] ) ;
            }
            else break ;
            a -- ;
        }
    }
}



int main()
{
    const int Size = 8 ;
    int A[Size] = { 45 , 32 , 1 , 65 , 23 , 19 , 10 , 7 } ;
    int B[Size] = { 12 , 58 , 9 , 98 , 42 , 48 , 71 , 8 } ;
    int C[Size] = { 92 , 22 , 5 , 25 , 61 , 17 , 34 , 2 } ;
    
    int* Array[] = { A , B , C } ;
     
    Functions Sorter[] = { &Bubble_Sort , &Selection_Sort , &Insertion_Sort } ;
    
    for( int _ = 0 ; _ < 3 ; _++ )
    {
        Print( Array[_] , Size ) ;
        Sorter[_]( Array[_] , Size ) ;
        Print( Array[_] , Size ) ;
    }
    return 1 ;
}
