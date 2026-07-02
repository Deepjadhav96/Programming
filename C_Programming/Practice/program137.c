#include<stdio.h>
#include<stdbool.h>

int CountChar(char *str, char ch)
{
    while(*str !='\0')
    {
        if(*str == ch)
        {
            return true;
            
        }
        str++;
    }
    return false;

}

int main()
{
    char ch[40] = {0};
    char cValue ;
    int bRet;

    printf("Enter a String: ");
    scanf("%[^\n]",ch);

    printf("Enter character that you want to check: ");
    scanf(" %c",&cValue);
    

    bRet = CheckChar(ch,cValue);

    if(bRet == true)
    {
        printf("Character is present...\n");
    }
    else
    {
        printf("Character is not present...\n");
    }
    return 0;
}