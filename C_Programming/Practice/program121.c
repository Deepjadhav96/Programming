#include<stdio.h>


int CountCapital(char *ch)
{
    int iCnt = 0;

    while ( *ch != '\0')
    {
        if(*ch >= 'A' && *ch <= 'Z')
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

    iRet = CountCapital(cArr);

    printf("Frequency of Capital letter is: %d\n",iRet);

    return 0;
}