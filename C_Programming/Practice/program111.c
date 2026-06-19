#include<stdio.h>
#include<stdbool.h>

bool ChkAlpha(char ch)
{
    if((ch >= 65 && ch <=90) || (ch>=97 && ch <= 123))
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

    bRet = ChkAlpha(cValue);

    if(bRet == true)
    {
        printf("It's character\n");
    }
    else
    {
        printf("It's not character\n");
    }

    return 0;
}