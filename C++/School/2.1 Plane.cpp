#include <iostream>
using namespace std ;
class Aeroplane
{
    int   Flight_no       ;
    char  Destination[20] ;
    float Distance , Fuel ;
    void  CALFUEL()
    {
        if      (Distance <= 1000)  Fuel = 500  ;
        else if (Distance <= 2000)  Fuel = 1100 ;
        else if (Distance  > 2000)  Fuel = 2200 ;
    }
public :
    void  FEEDINFO()
    {
        cout << "Input Flight Details\n" ;
        cout << "Enter Flight Number :>" ;
        cin  >> Flight_no                ;
        cout << "Enter Destination   :>" ;
        cin  >> Destination              ;
        cout << "Enter Distance      :>" ;
        cin  >> Distance                 ;
        CALFUEL()                        ;
    }
    void  SHOWINFO()
    {
        cout << "\n-Flight Details-"                ;
        cout << "\nFlight Number : " << Flight_no   ;
        cout << "\nDestination   : " << Destination ;
        cout << "\nDistance      : " << Distance    ;
        cout << "\nFuel          : " << Fuel        ;
    }
};

int main()
{
    Aeroplane X  ;
    X.FEEDINFO() ;
    X.SHOWINFO() ;
    return 0     ;
}
