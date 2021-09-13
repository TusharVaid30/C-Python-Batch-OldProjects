#include <iostream>
using namespace std ;

struct TIME 
{
    int hh , mm , ss ;
} ;

TIME ADD( TIME A , TIME B )
{
    TIME C ;
    C.ss = A.ss + B.ss ; 
    C.mm = A.mm + B.mm + C.ss/60 ; 
    C.hh = A.hh + B.hh + C.mm/60 ;
    C.ss %= 60 ;
    C.mm %= 60 ; 
    return C   ;
}

TIME GREATER( TIME A , TIME B )
{
    if( A.hh == B.hh )
    {
        if( A.mm == B.mm )
        {
            if( A.ss == B.ss ) 
            {
                cout << "Both are equal, Time : " ; 
                return A ;    
            }
            return A.ss > B.ss ? A : B ;
        }
        return A.mm > B.mm ? A : B ;
    }
    return A.hh > B.hh ? A : B ;
}

int main()
{
    TIME X , Y , Z ;
    cout << "Input Time 1 :> " ; cin >> X.hh >> X.mm >> X.ss ;
    cout << "Input Time 2 :> " ; cin >> Y.hh >> Y.mm >> Y.ss ;
    Z = ADD(X , Y) ;
    cout << "Time 1 : " << X.hh << " h " << X.mm << " m " << X.ss << " s." << endl  ;
    cout << "Time 2 : " << Y.hh << " h " << Y.mm << " m " << Y.ss << " s." << endl  ;
    cout << "Total  : " << Z.hh << " h " << Z.mm << " m " << Z.ss << " s." << endl  ;
    Z = GREATER(X , Y) ;
    cout << "Greater Time   : " << Z.hh  << " h "<< Z.mm  << " m "<< Z.ss  << " s." ; 
    return 1 ;
}
