#include<stdio.h>
#include<stdbool.h>

typedef unsigned int UINT;

bool ChkBit(UINT iNo, UINT iMask)
{
    UINT iAns = 0;

    iAns = iNo & iMask;

    if(iAns == iMask)
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
     long int iMask = 0X100000002;
    bool bRet;
    printf("Enter a Number:");
    scanf("%d",&iValue);

    bRet = ChkBit(iValue, iMask);

    if(bRet == true)
    {
        printf("1st and last(32Bit) Bit is on\n");
    }
    else
    {
        printf("1st and last(32Bit) Bit is off\n");
    }


    return 0;
}