#include <string.h>
#include <iostream>
using namespace std ;

char *Subjects[] = { 
                     "English  " , 
                     "Math     " ,
                     "Physics  " , 
                     "Chemistry" ,
                     "Computers" 
                   } ;

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
} ;

class TEST : public STUDENT 
{
    float English , Math      ,
          Physics , Chemistry ,
          ComputerScience     ;
    float * Subject[5]  = { &English , &Math      ,
                            &Physics , &Chemistry ,
                            &ComputerScience    } ;
    
    void Calculate_Total()
    {                  
        for ( int i = 0 ; i < 5 ; i++ ) Total_Marks += *Subject[i]  ; 
    }
    
protected :
    float Total_Marks ;

public    :
    Test()
    {
        Total_Marks = 0 ;
        for( int  i = 0 ; i < 5 ; i++ )
            *Subject[i] = 0 ;
    }
     
    void Get_Data()
    {
        for( int i = 0 ; i < 5 ; i++ )
        {
            cout << "Enter " << Subjects[i] << " Marks :>" ;
            cin  >> *Subject[i] ;
        }
        Calculate_Total() ; 
    }
    
    void Display_Data()
    {
        cout << " - Marks - \n" ;
        for( int i = 0 ; i < 5 ; i++ )
            cout << Subjects[i] << " Marks : " << *Subject[i] << endl ;
        cout << "Total Marks : " << Total_Marks ;
    }
} ;

class RESULT : public TEST
{
    float Percentage ;
    char  Grade      ;

public :
    
    RESULT() 
    {
        Percentage = 0 ;
        Grade = 'E' ;
    }
    
    void Calculate_Percentage()
    {
        Percentage = Total_Marks/5 ;
    }
    
    void Calculate_Grade()
    {
        Calculate_Percentage() ;
        if     (Percentage >= 90) Grade = 'A' ;
        else if(Percentage >= 75) Grade = 'B' ;
        else if(Percentage >= 60) Grade = 'C' ;
        else if(Percentage >= 40) Grade = 'D' ;
        else Grade = 'E' ;
    }
    
    void Display_Result()
    {
        Calculate_Grade() ; 
        cout << "\nPercentage : " << Percentage ;
        cout << "\nGrade      : " << Grade      ;
    }
} ;

int main()
{
    RESULT X ;
    X.Get_Data() ; X.Display_Data() ; X.Display_Result() ;
    return 0 ;
}
