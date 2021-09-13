#include <string.h>
#include <fstream>
#include <iostream>
using namespace std ;

const char V[] = { 'A' , 'E' , 'I' , 'O' , 'U' } ;

int Is_Vowel( char A )
{
    for( int i = 0 ; i < 5 ; i++ )
        if( toupper(A) == V[i] )
            return 1 ;
    return 0 ;
}

void Write()
{
    int size = 50   ;  char W[50] ;
    cout << "Inputting to file.\n:>" ; gets(W) ;
    ofstream F("Try.txt") ;
    F << W ;
    F.close()  ;
}

void Consonants()
{
    int Con = 0 ; char C  ;
    ifstream F("Try.txt") ;
    F.get(C) ;
    while( ! F.eof() )
    {
        if( C != ' ' && ! Is_Vowel(C) ) Con ++ ;
        F.get(C) ;
    }
    F.close() ;
    cout << Con << " Consonants present.\n" ;
}

void Uppercase_Vowels()
{
    int Vol = 0 ; char C  ;
    ifstream F("Try.txt") ;
    F.get(C) ;
    while( ! F.eof() )
    {
        for( int i = 0 ; i < 5 ; i++ )
            if( C == V[i] ) Vol ++ ; 
        F.get(C) ;
    }
    F.close() ;
    cout << Vol << " Uppercase Vowels present.\n" ;
}

void Words()
{
    int W = 1 ; char C[20]  ;
    ifstream F ("Try.txt")  ;
    F.getline(C , 20 , ' ') ;
    while( ! F.eof() )
    {
        W ++ ; 
        F.getline(C , 20 , ' ') ;
    }
    F.close() ;
    cout << W << " Words present.\n" ;
}

void Lines()
{
    int L = 1 ; char C[80]   ;
    ifstream F ("Try.txt")   ;
    F.getline(C , 80 , '\n') ;
    while( ! F.eof() ) 
    {
        L ++ ;
        F.getline(C , 80 , '\n') ;
    }
    F.close() ;
    cout << L << " Lines present.\n" ;
}

void The()
{
    int W = 0 ; char C[20]  ;
    ifstream F ("Try.txt")  ;
    F.getline(C , 20 , ' ') ;
    while( ! F.eof() )
    {
        if( strcmpi(C , "The") == 0 ) W ++ ; 
        F.getline(C , 20 , ' ') ;
    }
    F.close() ;
    cout << W << " occurence of \'The\'.\n" ;
}

int main()
{
    Write() ;
    Consonants() ;
    Uppercase_Vowels() ;
    Words() ;
    Lines() ;
    The() ;
    return 0 ;
}
