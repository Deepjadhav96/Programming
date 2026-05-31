#include<stdio.h>

int DollarToINR(int iNo)
{
  int iDollar = 0;

  iDollar = iNo * 70;

  return iDollar;
  
}
int  main()
{
    int iValue = 0;
    int iRet = 0;

    printf("Enter a value: \n");
    scanf("%d",&iValue);

    iRet = DollarToINR(iValue);
    printf("%d \n ",iRet);
    return 0;
}

///////////////////////////////////
///  Input: 5
///  Output: 350
///
///  Input: 4
///  Output: 280
///////////////////////////////////
