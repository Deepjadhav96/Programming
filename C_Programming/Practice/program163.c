#include<stdio.h>
#include<stdbool.h>

typedef unsigned int UINT;

bool ChkBit(UINT iNo)
{
    UINT iMask = 0x900;
    UINT Output = 0;


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

    bool bResult = 0;

    printf("Enter a Number:");
    scanf("%d",&iValue);


    bResult =ChkBit(iValue);
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