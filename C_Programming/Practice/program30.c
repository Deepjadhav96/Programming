#include<stdio.h>

void Table(int iNo)
{
    int iCnt = 0;
    int iRet = 1;
     if(iNo < 0)
     {
        iNo = -iNo;
     }
     for(iCnt = 10; iCnt >= 1; iCnt--)
     {
        iRet = iNo * iCnt;
        printf("%d ",iRet);
     }
     printf("\n");

     
}

int main()
{
    int iValue = 0;
    printf("Enter a number: \n");
    scanf("%d",&iValue);

    Table(iValue);
    return 0;
}

///////////////////////////////////
///  Input: 7
///  Output:70 63 56 49 42 35 28 21 14 7 
///
///  Input: 4
///  Output: 40 36 32 28 24 20 16 12 8 4
///////////////////////////////////

