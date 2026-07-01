#include<stdio.h>

typedef unsigned int UINT;

UINT ToggleBit(UINT iNo, UINT iMask)
{
    UINT iAns = 0;

    iAns = iNo ^ iMask;

    return iAns;


}

int main()
{
    UINT iValue = 0;
    UINT iMask = 0X240;
    UINT iResult = 0;

    printf("Enter a Number:");
    scanf("%d",&iValue);

    iResult =ToggleBit(iValue, iMask);
    printf("Modified number:%d\n ",iResult);

    return 0;
}