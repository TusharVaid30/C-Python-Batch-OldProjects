#include <string.h>
#include <iostream>
using namespace std ;

class Garment
{
    char  GCode[20] , GType[20] , GFabric[20] ;
    int   GSize     ;
    float GPrice    ;
    
    void  Assign()
    {
        float redu  ;
        if ( strcmpi(GFabric,"Cotton") == 0 )
             redu =   0 ;
        else 
             redu = 0.1 ;
             
        if ( strcmpi(GType  ,"Trouser") == 0 )
             GPrice = 1300  ;
        if ( strcmpi(GType  ,"Shirt"  ) == 0 )
             GPrice = 1100  ;
             
        GPrice -= redu*GPrice ;
    }
public :
    void  Input()
    {
        cout << "Input Garment Details\n"               ;
        cout << "Enter GCode   :>"    ;  cin >> GCode   ;
        cout << "Enter GType   :>"    ;  cin >> GType   ;
        cout << "Enter GSize   :>"    ;  cin >> GSize   ;
        cout << "Enter GFabric :>"    ;  cin >> GFabric ;
        Assign() ;
    }
    void  Display()
    {
        cout << "-Garment Details-"       ;
        cout << "\nGCode   : " << GCode   ;
        cout << "\nGType   : " << GType   ;
        cout << "\nGSize   : " << GSize   ;
        cout << "\nGFabric : " << GFabric ;
        cout << "\nGPrice  : " << GPrice  ;
    }
};

int main()
{
    Garment X   ;
    X.Input()   ;
    X.Display() ;
    return 0    ;
}
