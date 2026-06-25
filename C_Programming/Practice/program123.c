#include<stdio.h>


int Difference(char *ch)
{
    int iCnt1 = 0, iCnt2 = 0;

    while ( *ch != '\0')
    {
        if(*ch >= 'a' && *ch <= 'z')
        {
            iCnt1++;
        }
        else
        {
            iCnt2++;
        }
        ch++;
    }
    
    return iCnt1 - iCnt2;

}

int main()
{
    char cArr[20] = {'\0'};
    int iRet = 0;

    printf("Enter a string:");
    scanf("%[^'\n']s",cArr);

    iRet = Difference(cArr);

    printf("Difference between small and capital letter: %d\n",iRet);

    return 0;
}