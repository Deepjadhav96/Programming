#include<stdio.h>
#include<stdbool.h>

typedef unsigned int UINT;

bool ChkBit(UINT iNo, UINT iPos)
{
    UINT iMask = 0x1;
    UINT Output = 0;

    iMask = iMask << (iPos -1);

     Output = iNo & iMask;

    if(iMask == Output)
    {
        return true;
    }
    else
    {
        return false;
    }


}

int main()
{
    UINT iValue = 0;
    UINT iLocation = 0;
    bool bResult = 0;

    printf("Enter a Number:");
    scanf("%d",&iValue);

    printf("Enter a position:");
    scanf("%d",&iLocation);

    bResult =ChkBit(iValue,iLocation);
    if(bResult == true)
    {
        printf("Bit is on\n");
    }
    else
    {
        printf("Bit is off\n");
    }
    return 0;
}