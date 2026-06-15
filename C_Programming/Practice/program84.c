/*
Enter number of rows:3
Enter number of columns:4
#	*	#	*	
#	*	#	*	
#	*	#	*

*/

#include<stdio.h>

void pattern(int iRow, int iColumn)
{
    int i  = 0 , j = 0 ;
    for(i = 1; i <= iRow; i++)
    {
        for(j = 1; j <= iColumn; j++)
        {
           if(j % 2 == 0)
           {
            printf("*\t");
           }
           else
           {
            printf("#\t");
           }
        }
    }

    
    
    printf("\n");

}
int main()
{
    int iValue1 = 0 , iValue2 = 0;

    printf("Enter number of rows:");
    scanf("%d",&iValue1);

    printf("Enter number of columns:");
    scanf("%d",&iValue2);


    pattern(iValue1, iValue2);
    return 0;
}