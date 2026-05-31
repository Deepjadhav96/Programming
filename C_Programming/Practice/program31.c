#include<stdio.h>

void Display(int iNo)
{
  int iCnt = 0;

  if(iNo < 0)
  {
    iNo = -iNo;
  }

  for(iCnt = 1; iCnt <=iNo; iCnt++)
  {
    printf("* ");
  }

  for(iCnt = 1; iCnt <=iNo; iCnt++)
  {
    printf(" # ");
  }

  printf("\n");
}
int  main()
{
    int iValue = 0;

    printf("Enter a value: \n");
    scanf("%d",&iValue);

    Display(iValue);
    return 0;
}

///////////////////////////////////
///  Input: 5
///  Output: * * * * * # # # # #
///
///  Input: 4
///  Output: * * * * # # # #
///////////////////////////////////
