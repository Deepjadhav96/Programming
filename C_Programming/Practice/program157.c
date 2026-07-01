#include<stdio.h>

typedef unsigned int UINT;

UINT ChkBit(UINT iNo, UINT iPos)
{
    UINT iMask = 0x1;
    UINT Output = 0;

    iMask = iMask << (iPos -1);

    iMask = ~iMask;

     Output = iNo & iMask;

    return Output;

}

int main()
{
    UINT iValue = 0;
    UINT iLocation = 0;
    UINT iResult = 0;

    printf("Enter a Number:");
    scanf("%d",&iValue);

    printf("Enter a position:");
    scanf("%d",&iLocation);

    iResult =ChkBit(iValue,iLocation);
    printf("Number after Bit off %d\n",iResult);
    
    return 0;
}