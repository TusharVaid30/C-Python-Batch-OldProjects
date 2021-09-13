#include <string.h>
#include <iostream>
using namespace std ;

class outfit
{
    char  O_Type[20] , O_Code[20]  ;
    int   O_Size     ;
    float O_Price    ;
    void  int_price()
    {
        float redu ;
        if ( strcmpi(O_Fabric , "Denim")  )
            redu =    0 ;
        else 
            redu = 0.25 ;
        if ( strcmpi(O_Type  , "Trouser") )
            O_Price = 1500   ;
        if ( strcmpi(O_Type  , "Jacket" ) )
            O_Price = 2500   ;
        O_Price -= redu*O_Price ;
    }
public :
    char  O_Fabric[20] ;
    outfit()
    {
        O_Size = O_Price = 0 ;
        char* X[3] = { O_Type , O_Fabric , O_Code } ;
        for (int i = 0 ; i < 3 ; i++)
            strcpy(X[i] , "Not Inetialised") ;
    }
    void  Input()
    {
        cout << "Enter Outfit Code   :>" ;  cin >> O_Code   ;
        cout << "Enter Outfit Type   :>" ;  cin >> O_Type   ;
        cout << "Enter Outfit Size   :>" ;  cin >> O_Size   ;
        cout << "Enter Outfit Fabric :>" ;  cin >> O_Fabric ;
        int_price() ;
    }
    void  Display()
    {
        cout << "\nOutfit Code   : " << O_Code   ; 
        cout << "\nOutfit Type   : " << O_Type   ; 
        cout << "\nOutfit Size   : " << O_Size   ; 
        cout << "\nOutfit Fabric : " << O_Fabric ; 
        cout << "\nOutfit Price  : " << O_Price  ;
    }
};

int main()
{
    int i , Size = 1 ;
    outfit X1 , X2 , X3 , X4 , X5 ;
    outfit X[]  = { X1 , X2 , X3 , X4 , X5 } ;
    for( i = 0 ; i < Size ; i++)
    {
        cout << "Enter Oufit " << i + 1 << " Details.\n" ;
        X[i].Input()   ;
    }
    for( i = 0 ; i < Size ; i++)
    {
        cout << " \n\nOutfit " << i + 1 << " Details.  " ;
        X[i].Display() ;
    }
    return 0 ;
}
