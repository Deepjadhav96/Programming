#include<stdio.h>

#define PI 3.14 

double CircleArea(float fNo)
{
  double dArea = 0;
  
  dArea = PI * fNo * fNo;

  return dArea;

}
int main()
{
    float fValue = 0;
    double dRet = 0;

    printf("Enter a Radius: \n");
    scanf("%f",&fValue);

    dRet = CircleArea(fValue);

    printf("%lf \n",dRet);

    return 0;
}

///////////////////////////////////
/////   Input:5.3
/////   Output: 88.202606 
////
////     Input: 10.4
////     Output339.622375
////
///////////////////////////////////