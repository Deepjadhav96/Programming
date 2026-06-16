/*
Enter number of rows:
5
Enter number of columns:
5
1	2	3	4	5	
2	3	4	5	6	
3	4	5	6	7	
4	5	6	7	8	
5	6	7	8	9


*/

#include<stdio.h>


void Display(int iRow, int iCol)
{
    int i = 0, j = 0;

    for(i = 1; i <= iRow; i++)
    {
        for(j = 1; j <= iCol; j++)
        {
            printf("%d\t",(i + j- 1)); ///Best question of ASS 25
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