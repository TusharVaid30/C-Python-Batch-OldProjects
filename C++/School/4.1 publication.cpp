#include <iostream>
using namespace std ;

class Publication 
{
    char  Title[20] ;
    float Price   ;
public :
    void  Get_Data()
    {
        cout << "Input Publication Details.  \n" ;
        cout << "Enter Title :>" ;  cin >> Title ;
        cout << "Enter Price :>" ;  cin >> Price ;
    }
    void  Put_Data()
    {
        cout << "Publication Details.\n"    ;
        cout << "Title : " << Title << endl ;
        cout << "Price : " << Price << endl ;
    }
} ;

class Book : public Publication 
{
    int Page_Count ;
} ;

class Tape : public Publication
{
    float Playing_Time ;
} ;

int main()
{
    Book B ; Tape T ; 
    cout << "Enter Book details :\n" ; B.Get_Data() ; 
    cout << "Enter Tape details :\n" ; T.Get_Data() ;
    cout << "  - Book details -  \n" ; B.Put_Data() ; 
    cout << "  - Tape details -  \n" ; T.Put_Data() ; 
    
    return 1 ;
}

