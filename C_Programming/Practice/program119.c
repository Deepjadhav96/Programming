#include<stdio.h>
#include<stdbool.h>


bool ChkSpecial(char ch)
{
    if(ch >= 33  && ch <= 47)
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

    printf("Enter a character: ");
    scanf("%c",&cValue);

    bRet = ChkSpecial(cValue);

    if(bRet == true)
    {
        printf("It is a special character");
    }
    else
    {
        printf("It is a special character");
    }


    return 0;
}