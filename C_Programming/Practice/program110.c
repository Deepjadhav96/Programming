/*
Enter number of rows: 6
Enter number of columns: 6
1	2	3	4	5	6	
1	2	 	 	 	6	
1	 	3	 	 	6	
1	 	 	4	 	6	
1	 	 	 	5	6	
1	2	3	4	5	6

*/


#include<stdio.h>

void Display(int iRow, int iColumn)
{
    int i = 0, j = 0;

    if(iRow != iColumn)
    {
        printf("Invalid input");
        printf("Number of row and column should be same");
        return;
    }

    for(i = 1; i <= iRow; i++)
    {
        for(j = 1; j<= iColumn; j++)
        {
            if(i==1 || j==1 || j == iColumn || i == iRow || i == j)
            {
                printf("%d\t",j); 
            }
            else
            {
                printf(" \t");
            }
        }
        printf("\n");
    }


}


int main()
{
    int iValue1 = 0 , iValue2 = 0;

    printf("Enter number of rows: ");
    scanf("%d",&iValue1);

    printf("Enter number of columns: ");
    scanf("%d",&iValue2);

    Display(iValue1 , iValue2);
    return 0;
}