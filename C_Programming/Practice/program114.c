/*
Enter a character:
d
It's Small letter

Enter a character:
L
It's not Small letter

*/


#include<stdio.h>
#include<stdbool.h>

bool ChkSmall(char ch)
{
    if((ch >= 97 && ch <=122))
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

    bRet = ChkSmall(cValue);

    if(bRet == true)
    {
        printf("It's Small letter\n");
    }
    else
    {
        printf("It's not Small letter\n");
    }

    return 0;
}