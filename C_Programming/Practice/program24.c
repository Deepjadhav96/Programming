#include<stdio.h>
void OddDisplay(int iNo)
{
     int iCnt = 0;

    for(iCnt = 1; iCnt <= iNo; iCnt++)
    {
        if(iCnt % 2 != 0)
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

    OddDisplay(iValue);
    return 0;
}

///////////////////////////////////
///  Input: 5 
///  Output: 1 	3 	5 	 
///
///  Input: 8
///  Output: 1  3  5  7 
///////////////////////////////////
