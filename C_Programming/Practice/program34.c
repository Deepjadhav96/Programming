#include<stdio.h>

int OddFactorial(int iNo)
{
   int iCnt = 0;
   int iOddFact = 1;

   if(iNo < 0)
   {
    iNo = -iNo;
   }

   for(iCnt = 1; iCnt <= iNo; iCnt = iCnt + 2)
   {
        iOddFact = iOddFact * iCnt;
       
   }

    return iOddFact;
}
int  main()
{
    int iValue = 0;
    int iRet = 0;

    printf("Enter a value: \n");
    scanf("%d",&iValue);

    iRet = OddFactorial(iValue);
    printf("%d \n",iRet);
    return 0;
}

///////////////////////////////////
///  Input: 5
///  Output: 15 (5 * 3 * 1)
///
///  Input: 10
///  Output: 945 (9 * 7 * 5 * 3 * 1)
///////////////////////////////////
