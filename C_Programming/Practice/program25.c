#include<stdio.h>
void MultipleDisplay(int iNo)
{
     int iCnt = 0;

    for(iCnt = iNo; iCnt <= (5 * iNo); iCnt++)
    {
        if(iCnt % iNo  == 0)
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

    MultipleDisplay(iValue);
    return 0;
}

///////////////////////////////////
///  Input: 4
///  Output: 4 8 12 16 20	 
///
///  Input: 8
///  Output: 1  3  5  7 
///////////////////////////////////
