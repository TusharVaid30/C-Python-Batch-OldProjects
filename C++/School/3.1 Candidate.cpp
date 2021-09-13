#include <string.h>
#include <iostream>
using namespace std ;

class Candidate
{
    long  RNo      ;
    float Score    ;
    char  Name[20] , Remarks[20] ;
    void  AssignRem() 
    {
        if (Score >= 50)
           strcpy( Remarks , "Selected    " ) ;
        else 
           strcpy( Remarks , "Not Selected" ) ;
    }
public :
    void  Enter()
    {
        cout << "Enter Candidate Rollno. :>" ;
        cin  >> RNo     ;
        cout << "Enter Candidate Name    :>" ;
        cin  >> Name    ;
        cout << "Enter Candidate Score   :>" ;
        cin  >> Score   ;
        AssignRem()     ;
    }
    void  Display()
    {
        cout << "\nCandidate Name    : " << Name    ;
        cout << "\nCandidate Rollno. : " << RNo     ;
        cout << "\nCandidate Remarks : " << Remarks ;
        cout << "\nCandidate Score   : " << Score   ;
    }
    float  Return_Score()
    {
        return Score   ;
    } 
    char*  Return_Remarks()
    {
        return Remarks ;
    }
    char*  Return_Name()
    {
        return Name    ;
    }
};

int main()
{
    char Search_Name[20];
    int  i  ,  Size = 1 , Found = 0 ;
    Candidate   X1 , X2 , X3 , X4 , X5 ;
    Candidate X[] = { X1 , X2 , X3 , X4 , X5 } ;
    for ( i = 0 ;  i < Size  ; i++)
    {
        cout << "Input Candidate " << i + 1 << " Details.\n" ;
        X[i].Enter() ;
    }
    for ( i = 0 ;  i < Size  ; i++)
    {
        cout << "\nCandidate "     << i + 1 << " Details."   ;
        X[i].Display();
    }
    cout << "\n  -Selected Candidates-  \n " ;
    for ( i = 0 ;  i < Size  ; i++)
    {
        if ( strcmpi(X[0].Return_Remarks() , "Selected") )
            X[i].Display();
    }
    cout << "\n\nInput Candidate's Name \n:>" ;
    cin  >> Search_Name ;
    for ( i = 0 ;  i < Size  ; i++)
    {
        if ( strcmpi(X[0].Return_Name() , Search_Name) == 0 )
        {
            cout << "\nFound Candidate.\n" ;
            X[i].Display()  ;
            Found = 1 ;
        }
    }
    if( !Found ) cout << "\nNo Candidate was found with that name." ;      
    return 0 ;    
}
