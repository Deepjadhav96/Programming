#include<stdio.h>
int FactDiff(int iNo)
{
    if(iNo <= 0)
    {
        return -1;
    }
    
    int iCnt1 = 0;
    int iSum1 = 0;
    for(iCnt1 = 1; iCnt1 <= iNo/2; iCnt1++)
    {
        if(iNo % iCnt1 == 0)
        {
             iSum1 = iSum1 + iCnt1; 
             
        }
    }
    
    int iCnt2 = 0;
    int iSum2 = 0;
    for(iCnt2 = 1; iCnt2 <= iNo; iCnt2++)
    {
        if(iNo % iCnt2 >= 1)
        {
            iSum2 = iSum2 + iCnt2; 
        }
    }

    return iSum1 - iSum2;
}
int main()
{
    int iValue = 0;
    int iRet = 0;

    printf("Enter a number: \n");
    scanf("%d",&iValue);

    iRet = FactDiff(iValue);
    printf("%d",iRet);
    printf("\n");

    return 0;
}

///////////////////////////////////
///
///  Input: 12
///  Output: -34 (16 - 50)
///
///  Input: 10
///  Output: -29 (8 - 37)
///////////////////////////////////
