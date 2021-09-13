#include <iostream>
using namespace std ;

unsigned int Count( int L[] , int N = 10 )
{
    int x = 0 ;
    for(int i = 0 ; i < N ; i++)
            if(L[i]%7 == 0) 
                 x++ ;
    return x ;
}
int main()
{
    int length     ;
    cout << "Length of the list :>" ;
    cin  >> length ;
    int x[length]  ;
    
    for(int i = 0  ; i < length ; i++)
    {
        cout << "Enter element " << i << " :>" ;
        cin  >> x[i] ;
    }
    cout << Count(x , length) 
         << " multiples of Seven are present." ;
         
    return 0;
}
