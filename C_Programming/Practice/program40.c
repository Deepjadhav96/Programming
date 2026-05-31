#include<stdio.h>

#define SqMeter 0.0929

double SquareMeter(float fSqfeet)
{
 
    double dSqmeter = 0.0;
    dSqmeter = SqMeter * fSqfeet;

    return dSqmeter;

}
int main()
{
    float fValue = 0.f;
    double  iRet = 0;

    printf("Enter area in Square feet :\n");
    scanf("%f",&fValue);

   
    iRet = SquareMeter(fValue);

    printf("%f Square meters\n",iRet);

    return 0;
}