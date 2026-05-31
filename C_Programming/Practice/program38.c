#include<stdio.h>

double KMtoMeter(int iNo)
{
  int  fMeter = 1;

  fMeter = iNo * 1000;

  return fMeter;
}
int main()
{
    int iValue = 0;
    
    int  iRet = 0;

    printf("Enter a Distance: \n");
    scanf("%d",&iValue);

   
    iRet = KMtoMeter(iValue);

    printf("%d meters\n",iRet);

    return 0;
}

///////////////////////////////////
/////   Input:5
/////   Output: 5000 meters 
////
////     Input: 10
////     Output: 10000 meters
///////////////////////////////////