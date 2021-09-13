#include <string.h>
#include <fstream>
#include <iostream>
using namespace std ;

class Travel
{
    long Travel_Code ;
    char Place[20]   ;
    int  No_of_Buses , No_of_Travellers ;
public :
    Travel()
    {
        Travel_Code = 201 ;
        No_of_Buses = 1   ;
        No_of_Travellers = 10 ; 
        strcpy(Place , "Nainital") ;
    }
    void New_Travel()
    {
        cout << "Enter Travel Code :>" ; cin >> Travel_Code ;
        cout << "Enter Travellers  :>" ; cin >> No_of_Travellers ;
        cout << "Enter Place       :>" ; cin >> Place   ;
        if     (No_of_Travellers >= 40) No_of_Buses = 3 ;
        else if(No_of_Travellers >= 20) No_of_Buses = 2 ;
        else No_of_Buses = 1 ;
    }
    void Show_Travel() 
    {
        cout << "Travel Code : " << Travel_Code      << endl ;
        cout << "Travellers  : " << No_of_Travellers << endl ;
        cout << "Place       : " << Place            << endl ;
        cout << "Buses       : " << No_of_Buses      << endl ;
    }
    int Return_Bus()
    {
        return No_of_Buses ;
    }
    ~Travel()
    {
        cout << "Object is being destroyed...\n" ;
    }
} ;

void Add_One_Record()
{
    Travel T ;
    cout << "Enter Travel Details.\n" ;
    T.New_Travel() ;
    ofstream F("TRAVEL2.DAT" , ios :: binary | ios :: app ) ;
    F.write((char*)&T , sizeof(T)) ;
    F.close() ;
}

void Add_Many_Record()
{
    int I ;
    cout << "How many Records are to be added? :>" ;
    cin  >> I ;
    for( int i = 0 ; i < I ; i ++ )
    {
        Add_One_Record() ;
    }
}

void Add_Record()
{
    char C ;
    do{
        Add_One_Record() ;
        cout << "Repeat Again ? ( Y/N ) :>" ;
        cin  >> C ;
    }while( C == 'Y' ) ;
}

void Display_All_Record()
{
    Travel T ;
    ifstream F("TRAVELS2.DAT" , ios :: binary | ios :: in) ;
    F.read((char*)&T , sizeof(T)) ;
    while( ! F.eof() )
    {
        T.Show_Travel() ;
        F.read((char*)&T , sizeof(T)) ;
    }
    F.close() ;
}

void Display_Record()
{
    Travel T ; 
    ifstream F("TRAVEL2.DAT" , ios :: binary | ios :: in) ;
    F.read((char*)&T , sizeof(T)) ;
    while( ! F.eof() )
    {
        if( T.Return_Bus() > 2 ) T.Show_Travel() ;
        F.read((char*)&T , sizeof(T)) ;
    }
    F.close() ;
}
    
int main()
{
    int i ; char C ;
    do{
        cout << " 1 : Add one new Record ." << endl ;
        cout << " 2 : Add  n  new Records." << endl ;
        cout << " 3 : Add   many  Records." << endl ; 
        cout << " 4 : Display all Records." << endl ;
        cout << " 5 : Display where Bus>2." << endl ;
        cout << "Enter Option :>" ; cin >> i ;
        switch(i)
        {
            case 1 : Add_One_Record()     ; break ; 
            case 2 : Add_Many_Record()    ; break ;
            case 3 : Add_Record()         ; break ;
            case 4 : Display_All_Record() ; break ;
            case 5 : Display_Record()     ; break ;
            default: cout << "Invalid Input." ;
        }
        cout << "Repeat again? ( Y/N ) :>" ; cin >> C ;
    }while( C == 'Y' ) ;
    return 1 ; 
}
