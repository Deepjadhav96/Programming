#include<stdio.h>


int CountSmall(char *ch)
{
    int iCnt = 0;

    while ( *ch != '\0')
    {
        if(*ch >= 'a' && *ch <= 'z')
        {
            iCnt++;
        }
        ch++;
    }
    
    return iCnt;

}

int main()
{
    char cArr[20] = {'\0'};
    int iRet = 0;

    printf("Enter a string:");
    scanf("%[^'\n']s",cArr);

    iRet = CountSmall(cArr);

    printf("Frequency of Capital letter is: %d\n",iRet);

    return 0;
}