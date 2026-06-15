/*
Enter number of rows:5
Enter number of columns:4
A	A	A	A	
B	B	B	B	
C	C	C	C	
D	D	D	D	
E	E	E	E
*/

#include<stdio.h>

void pattern(int iRow, int iColumn)
{
    int i  = 0 , j = 0 ;
    char ch;

    for(i = 1,ch='A'; i <= iRow; i++,ch++)
    {
        for(j = 1; j <= iColumn; j++)
        {
          printf("%c\t",ch);
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