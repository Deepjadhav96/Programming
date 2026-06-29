/*
Enter a string:Marvellous Info System
White space count is:2
*/

#include<stdio.h>

int CountWhite(char *str)
{
    int iCount = 0;
    while (*str != '\0')
    {
       if(*str ==' ')
       {
        iCount++;
       }
        str++;
    }
    return iCount;
    
}


int main()
{
    char Arr[20] = {0};
    int iRet = 0;

    printf("Enter a string:");
    scanf("%[^'\n']s",Arr);

    iRet = CountWhite(Arr);
    printf("White space count is:%d\n",iRet);
    return 0;
}