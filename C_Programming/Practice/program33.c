#include<stdio.h>

int EvenFactorial(int iNo)
{
   int iCnt = 0;
   int iEvenFact = 1;

   if(iNo < 0)
   {
    iNo = -iNo;
   }

   for(iCnt = 2; iCnt <= iNo; iCnt = iCnt + 2)
   {
        iEvenFact = iEvenFact * iCnt;
       
   }

    return iEvenFact;
}
int  main()
{
    int iValue = 0;
    int iRet = 0;

    printf("Enter a value: \n");
    scanf("%d",&iValue);

    iRet = EvenFactorial(iValue);
    printf("%d \n",iRet);
    return 0;
}

///////////////////////////////////
///  Input: 5
///  Output: 8 (4 * 2)
///
///  Input: 10
///  Output: 3840 (10 * 8 * 6 * 4 * 2)
///////////////////////////////////
