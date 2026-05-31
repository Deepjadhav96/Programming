#include<stdio.h>

int FactorialDiff(int iNo)
{
   int iCnt = 0;
   int iOddFact = 1;
   int iEvenFact = 1;

   if(iNo < 0)
   {
    iNo = -iNo;
   }

   for(iCnt = 1; iCnt <= iNo; iCnt = iCnt + 2)
   {
        iOddFact = iOddFact * iCnt;
       
   }

    for(iCnt = 2; iCnt <= iNo; iCnt = iCnt + 2)
   {
        iEvenFact = iEvenFact * iCnt;
       
   }

   return iEvenFact - iOddFact;

}
int  main()
{
    int iValue = 0;
    int iRet = 0;

    printf("Enter a value: \n");
    scanf("%d",&iValue);

    iRet = FactorialDiff(iValue);
    printf("%d \n",iRet);
    return 0;
}

///////////////////////////////////
///  Input: 5
///  Output: -7 (8-15)
///
///  Input: 10
///  Output: 2895 (3840-945) 
///////////////////////////////////
