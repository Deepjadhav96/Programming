#include<stdio.h>
void Table(int iNo)
{
    int iCnt = 0;
    int iRet = 1;
     if(iNo < 0)
     {
        iNo = -iNo;
     }
     for(iCnt = 1; iCnt <= 10; iCnt++)
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
///  Output: 7 14 21 28 35 42 49 56 63 70 
///
///  Input: 4
///  Output: 4 8 12 16 20 24 28 32 36 40
///////////////////////////////////
