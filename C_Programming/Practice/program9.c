//Assignment No 3
#include<stdio.h>

void PrintEven(int iNo)
{
    int iCount = 0;
    if(iNo < 0)                                                 //Input filter.
    {
        printf("Invalid Input\n");
        return;
    }

    for(iCount = 2; iCount <= iNo*2; iCount++)
    {
        if(iCount % 2 == 0)
        {
         printf("%d",iCount);
        }
    }

}
int main()
{
    int iValue = 0;

    printf("Enter a number from user: \n");
    scanf("%d",&iValue);

    PrintEven(iValue);

    
    return 0;
}