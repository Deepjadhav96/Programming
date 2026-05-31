#include<stdio.h>

typedef int BOOL;

#define TRUE 1
#define FALSE 0


BOOL ChkVowel(char cValue)
{
    if(cValue == 'a'||  cValue =='A' || cValue =='e' || cValue =='E' || cValue =='i' || cValue =='I' || cValue =='O' || cValue =='o' ||cValue =='U' || cValue =='u')
    {
        return TRUE;
    }
    else
    {
        return FALSE;
    }

}
int main()
{
    char cValue = '\0';

    printf("Enter a character: \n");
    scanf("%c",&cValue);

    BOOL bRet = FALSE;

    bRet = ChkVowel(cValue);
    if(bRet == TRUE)
    {
        printf("It is Vowel \n");
    }
    else
    {
        printf("It is not Vowel \n");
    }
    return 0;

}

/////////////////////////////////////////////
//
//  Input : e
//  Output: True 
//
//  Input : a
//  Output: True 
// 
//  Input : D
//  Output: False 
//
///////////////////////////////////////////////