#include<stdio.h>
void NonFact(int iNo)
{
    if(iNo <= 0)
    {
        return;
    }

    int iCnt = 0;

    for(iCnt = 1; iCnt <= iNo; iCnt++)
    {
        if(iNo % iCnt >= 1)
        {
            printf("%d \t",iCnt);
        }
    }
    
    printf("\n");
}
int main()
{
    int iValue = 0;

    printf("Enter a number: \n");
    scanf("%d",&iValue);

    NonFact(iValue);
    return 0;printf("\n");
}

///////////////////////////////////
///
///  Input: 12
///  Output: 5 	7 	8 	9 	10  11 
///
///  Input: 15 
///  Output: 4 	6 	8 	9 	10 	11 	12 	13  14
///////////////////////////////////
