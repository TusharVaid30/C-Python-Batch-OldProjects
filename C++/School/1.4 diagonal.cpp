#include<iostream>
using namespace std;

int Diagonal(int A[10][10], int Length)
{
    int Sum = 0 ;
    for( int i = 0 ; i < Length ; i ++ )
    {
        for( int j = 0 ; j < Length ; j ++ )
        {
            if( i == (Length - j - 1) || i == j ) 
            {
                cout  << A[i][j] << "  " ;
                Sum   += A[i][j] ;
            }
            else cout << "   " ; 
        }
        cout << endl ;
    }
    return Sum ; 
}

int main()
{
    int A[10][10] , Length , i , j ;
    cout << "Enter size of Square Array :>" ; cin  >> Length ;
    
    for( i = 0 ; i < Length ; i ++ )
    {
        cout << "Row " << i << endl ;
        for( j = 0 ; j < Length ; j ++ )
        {
            cout << "Enter element " << j << " :>" ;
            cin  >> A[i][j] ;
        }
    }
    cout << "Array :" << endl ;
    for( i = 0 ; i < Length ; i ++ )
    {
        for( j = 0 ; j < Length ; j ++ ) cout << A[i][j] << "  " ;
        cout << endl ; 
    }
    
    cout << "Sum of elements in diagonals :" Diagonal(A , Length) ;
    return 0 ;
}
