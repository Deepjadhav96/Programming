#include<stdio.h>
int SumNonFact(int iNo)
{
    if(iNo <= 0)
    {
        return -1;
    }

    int iCnt = 0;
    int iSum = 0;

    for(iCnt = 1; iCnt <= iNo; iCnt++)
    {
        if(iNo % iCnt >= 1)
        {
            iSum = iSum + iCnt;
        }
    }
    
    return iSum;
}
int main()
{
    int iValue = 0;
    int iRet = 0;

    printf("Enter a number: \n");
    scanf("%d",&iValue);

    iRet = SumNonFact(iValue);

    printf("%d\n",iRet);
    return 0;
}

///////////////////////////////////
///
///  Input: 12
///  Output: 50
///
///  Input: 10
///  Output:37
///////////////////////////////////
