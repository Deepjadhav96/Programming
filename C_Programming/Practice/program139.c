#include<stdio.h>

int FirstChar(char *str, char ch)
{
    int iIndex = 0;
    while(*str !='\0')
    {
        if(*str == ch)
        {
            break;  
        }
        else if(*str != ch)
        {
            return;
        }
        iIndex++;
        str++;
    }
    return iIndex;
    
}

int main()
{
    char ch[40] = {0};
    char cValue ='\0';
    int iRet=0;

    printf("Enter a String: ");
    scanf("%[^\n]",ch);

    printf("Enter character to check position : ");
    scanf(" %c",&cValue);
    
    iRet = FirstChar(ch, cValue);

    printf("Frequency of character is: %d\n",iRet);
}