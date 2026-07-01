#include<stdio.h>
#include<stdbool.h>

typedef unsigned int UINT;

bool ChkBit(UINT iNo, UINT iPos, UINT iPos2)
{
    UINT iMask ,iMask1 = 0X1, iMask2 = 0X1;
    UINT Output = 0;

    iMask1 = iMask1 << (iPos -1);
    iMask2 = iMask2 << (iPos -1);

    iMask = iMask1 ^ iMask2;

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
    UINT iLocation = 0, iLocation2 = 0;
    bool bResult = 0;

    printf("Enter a Number:");
    scanf("%d",&iValue);

    printf("Enter a first position:");
    scanf("%d",&iLocation);

    printf("Enter a second position:");
    scanf("%d",&iLocation2);

    bResult =ChkBit(iValue,iLocation,iLocation2);
    if(bResult == true)
    {
        printf("TRUE\n");
    }
    else
    {
        printf("FALSE\n");
    }
    return 0;
}