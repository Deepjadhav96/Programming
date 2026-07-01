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
    UINT iMask = 0X20010;
    bool bRet;
    printf("Enter a Number:");
    scanf("%d",&iValue);

    bRet = ChkBit(iValue, iMask);

    if(bRet == true)
    {
        printf("5th and 8th Bit is on\n");
    }
    else
    {
        printf("5th and 8th Bit is off\n");
    }


    return 0;
}