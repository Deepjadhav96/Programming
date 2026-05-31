#include<stdio.h>
int Factorial(int iNo)
{
     int iCnt = 0;
     int iFact = 1;

    for(iCnt = iNo; iCnt >= 1; iCnt--)
    {
        iFact = iFact * iCnt;
    }

    return iFact;   
}
int main()
{
    int iValue = 0;
    int iRet = 0;
    printf("Enter a number: \n");
    scanf("%d",&iValue);

    iRet = Factorial(iValue);
    printf("%d \n",iRet);
    return 0;
}

///////////////////////////////////
///  Input: 5
///  Output:120	 
///
///  Input: 6
///  Output:720 
///////////////////////////////////
