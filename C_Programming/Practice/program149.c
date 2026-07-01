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
    UINT iMask = 0X1c0;
    bool bRet;
    printf("Enter a Number:");
    scanf("%d",&iValue);

    bRet = ChkBit(iValue, iMask);

    if(bRet == true)
    {
        printf("7th, 8th and 9th Bit is on\n");
    }
    else
    {
        printf("7th, 8th and 9th Bit is off\n");
    }


    return 0;
}