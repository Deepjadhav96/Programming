#include<stdio.h>

typedef unsigned int UINT;

UINT CountOne(UINT iNo)
{
    UINT iCount = 0;

    while (iNo != 0)
    {
        if((iNo & 1)==1)
        {
               iCount++;
        }
        iNo = iNo >> 1;
    }
    return iCount;
}

int main()
{
    UINT iValue = 0;
   
    UINT iResult = 0;

    printf("Enter a Number:");
    scanf("%d",&iValue);

  

    iResult =CountOne(iValue);
    printf("Count of 1's are :%d\n",iResult);
    
    return 0;
}