/*
Enter number of rows:4
Enter number of columns:4
4	4	4	4	
3	3	3	3	
2	2	2	2	
1	1	1	1
*/

#include<stdio.h>

void pattern(int iRow, int iColumn)
{
    int i  = 0 , j = 0 ;
    

    for(i = iRow; i >= 1; i--)
    {
        for(j = 1; j <= iColumn; j++)
        {
          printf("%d\t",i);
        }
        printf("\n");
    }

    
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