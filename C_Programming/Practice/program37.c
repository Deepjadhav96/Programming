#include<stdio.h>

double RectArea(float fNo1 , float fNo2)
{
  double dArea = 0;
  
  dArea =  fNo1 * fNo2;

  return dArea;

}
int main()
{
    float fValue1 = 0;
    float fValue2 = 0;

    double dRet = 0;

    printf("Enter a Width: \n");
    scanf("%f",&fValue1);

    printf("Enter a height: \n");
    scanf("%f",&fValue2);

    dRet = RectArea(fValue1,fValue2);

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