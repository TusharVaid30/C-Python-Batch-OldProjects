#define Variable_Name( x ) #x 
#include <string.h>
#include <iostream>
using namespace std ;

class STUDENT
{
    char         Name[20] ;
    unsigned int RollNo   ;
    
protected :
    unsigned int Class    ;

public    :
    STUDENT()
    {
        strcpy(Name , "Not Assigned") ;
        RollNo = Class = 0            ;
    }
    void Input()
    {
        cout << "Input Student Details. \n" ;
        cout << "Enter Name   :>" ;  cin >> Name   ;
        cout << "Enter Class  :>" ;  cin >> Class  ;
        cout << "Enter RollNo :>" ;  cin >> RollNo ;
    }
    void Display()
    {
        cout << "Student Details. \n" ;
        cout << "Name   : " << Name   ;
        cout << "Class  : " << Class  ;
        cout << "RollNo : " << RollNo ;
    }
};

class TEST
{
    float English , Math      ,
          Physics , Chemistry ,
          ComputerScience     ;
    float * Subject[5]  = { &English , &Math      ,
                            &Physics , &Chemistry ,
                            &ComputerScience    } ;
    
    void Calculate_Total()
    {                  
        for ( int i = 0 ; i < 5 ; i++ )
            TotalMarks += *Subject[i]  ;
    }
    
protected :
    float TotalMarks ;

public    :
    Test()
    {
        for( int i = 0 ; i < 5 ; i++ )
            *Subject[i] = 0 ;
    }
     
    void getData()
    {
        for( int i = 0 ; i < 5 ; i++ )
        {
            cout << "Enter " << Variable_Name(Variable_Name(*Subject[i])) << " Marks :>" ;
            cin  >> *Subject[i] ;
        }
    }
    
    void displayData()
    {
        for( int i = 0 ; i < 5 ; i++ )
            cout << Variable_Name(*Subject[i]) << " Marks : " << *Subject[i] ;
        cout << "Total Marks : " << TotalMarks ;
    }
} ;

int main()
{
    TEST t ;
    t.getData() ;
    t.displayData() ;
    return 0 ;
}
