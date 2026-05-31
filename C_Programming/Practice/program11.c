//Ass 3 (3)
#include<stdio.h>

void DisplayEvenFactor(int iNo)
{
    int iCount = 0;

    if(iNo < 0)
    {
        iNo = -iNo;
    }

    for(iCount = 1; iCount <= iNo; iCount++)
    {
        if(iNo % iCount == 0 && iCount % 2 == 0)
        {
            printf("%d \n",iCount);
        }
    }

        printf("\n");

}


int main()
{
    int iValue = 0;

    printf("Enter a number: \n");
    scanf("%d",&iValue);

    DisplayEvenFactor(iValue);
    return 0;
}