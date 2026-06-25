/*
Enter a character:
a
It's not Capital letter

Enter a character:
Z
It's Capital letter

*/


#include<stdio.h>
#include<stdbool.h>

bool ChkCapital(char ch)
{
    if((ch >= 65 && ch <=90))
    {
        return true;
    }
    else
    {
        
        return false;
    }

}


int main()
{
    char cValue = '\0';

    bool bRet = false;

    printf("Enter a character:\n");
    scanf("%c",&cValue);

    bRet = ChkCapital(cValue);

    if(bRet == true)
    {
        printf("It's Capital letter\n");
    }
    else
    {
        printf("It's not Capital letter\n");
    }

    return 0;
}