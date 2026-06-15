/*
Enter number of rows:4
Enter number of columns:4
A	B	C	D	
A	B	C	D	
A	B	C	D	
A	B	C	D
*/

#include<stdio.h>

void pattern(int iRow, int iColumn)
{
    int i  = 0 , j = 0 ;
    char ch;

    for(i = 1; i <= iRow; i++)
    {
        for(j = 1,ch='A'; j <= iColumn; j++,ch++)
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