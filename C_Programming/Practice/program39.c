#include<stdio.h>

#define TEMP1 32
#define TEMP2 5/9

double FHtoCS(float fTemp)
{
  float fCels = 0.0f;
  fCels = ( (fTemp - TEMP1) * TEMP2);

  return fCels ;
}
int main()
{
    float fValue = 0.f;
    
    double  iRet = 0;

    printf("Enter temprature in Fahrenheit \n");
    scanf("%f",&fValue);

   
    iRet = FHtoCS(fValue);

    printf("%f meters\n",iRet);

    return 0;
}