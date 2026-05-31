//Ass 3 (3)
#include<stdio.h>

void DisplayFactor(int iNo)
{
    int iCount = 0;

    for(iCount = 1; iCount <= iNo; iCount++)
    {
        if(iNo % iCount == 0 )//&& iCount % 2 == 0)
        {
            printf("%d \t",iCount);
        }
    }

    printf("\n");

}


int main()
{
    int iValue = 0;

    printf("Enter a number: \n");
    scanf("%d",&iValue);

    DisplayFactor(iValue);
    return 0;
}