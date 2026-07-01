#include<stdio.h>

typedef unsigned int UINT;

UINT OffBit(UINT iNo, UINT iMask)
{
    UINT iAns = 0;

    iMask = ~iMask;  // 0100 0000 = 1011 1111

    iAns = iNo & iMask;

    return iAns;


}

int main()
{
    UINT iValue = 0;
    UINT iMask = 0X40;
    UINT iResult = 0;

    printf("Enter a Number:");
    scanf("%d",&iValue);

    iResult =OffBit(iValue, iMask);
    printf("Modified number:%d\n ",iResult);

    


    return 0;
}