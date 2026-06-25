/*
check whether it is digit or not.
*/


#include<stdio.h>
#include<stdbool.h>

bool ChkDigit(char ch)
{
    if((ch >= 48 && ch <=57))
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
    int iValue = '\0';

    bool bRet = false;

    printf("Enter a character:\n");
    scanf("%d",&iValue);

    bRet = ChkDigit(iValue);

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