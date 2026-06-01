#include<stdio.h>
void RangeSum(int iStart, int iEnd)
{
   
     

        while (iStart <= iEnd )
        {
         
            printf("%d \t",iEnd);
               
            iEnd--;
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