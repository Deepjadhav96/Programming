/*
Enter number of rows:
5
Enter number of columns:
5
2	4	6	8	10	
1	3	5	7	9	
2	4	6	8	10	
1	3	5	7	9	
2	4	6	8	10	


*/

#include<stdio.h>


void Display(int iRow, int iCol)
{
    int i = 0, j =0, iCount = 0;

    for(i = 1; i <= iRow; i++)
    {
        if(i % 2 != 0)
        {
            for(j = 1,iCount = 2; j <= iCol; j++,iCount = iCount + 2)
            {
                printf("%d\t",iCount);
            }
        }
        else
        {
            for(j = 1,iCount = 1; j <= iCol; j++,iCount = iCount + 2)
            {
                printf("%d\t",iCount);
            }
        }
        
       printf("\n");
    }
}

int main()
{
    int iValue1 = 0, iValue2 = 0;

    printf("Enter number of rows:\n");
    scanf("%d",&iValue1);

    printf("Enter number of columns:\n");
    scanf("%d",&iValue2);

    Display(iValue1 , iValue2);
    return 0;
}