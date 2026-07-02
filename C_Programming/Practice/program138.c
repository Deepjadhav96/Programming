#include<stdio.h>

int CountChar(char *str, char ch)
{
    int iCount = 0;
    while(*str !='\0')
    {
        if(*str == ch)
        {
            iCount++;
        }
        str++;
    }
    return iCount;
    
}

int main()
{
    char ch[40] = {0};
    char cValue ='\0';
    int iRet=0;

    printf("Enter a String: ");
    scanf("%[^\n]",ch);

    printf("Enter character that you want to check: ");
    scanf(" %c",&cValue);
    
    iRet = CountChar(ch, cValue);

    printf("Frequency of character is: %d\n",iRet);
}