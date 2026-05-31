#include<stdio.h>

int Display(int iNo, int iFrequency)
{

    int iCnt = 0;
    
    if(iFrequency < 0)
    {
        return -1;
        
    }

    for(iCnt = 1; iCnt <= iFrequency; iCnt++)
    {
        printf("%d \n",iNo);
    }
}



int main()
{

    int iValue = 0;
    int iCount = 0 ;

    printf("Enter a number : ");
    scanf("%d",&iValue);

    printf("Enter frequency : ");
    scanf("%d",&iCount);

    Display(iValue,iCount);


    return 0;
}