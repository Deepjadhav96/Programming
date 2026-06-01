#include<stdio.h>
void RangeSum(int iStart, int iEnd)
{
    int iSum = 0;
     if(iStart > iEnd || iStart < 0)
    {
        printf("Invalid Range: ");
    }
    else
    {
        while (iStart <= iEnd )
        {
                
            iSum = iSum + iStart;
                
                
            iStart++;

        }
         printf("%d \t",iSum);
   
    }
    
    printf("\n");

}
int main()
{
    int iValue1 = 0 , iValue2 = 0;

    printf("Enter starting point: ");
    scanf("%d",&iValue1);

    printf("Enter ending point : ");
    scanf("%d",&iValue2);

    RangeSum(iValue1 , iValue2);
    return 0;
}