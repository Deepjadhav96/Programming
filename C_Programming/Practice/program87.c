/*
Enter number of rows:4
Enter number of columns:4
A	B	C	D	
a	b	c	d	
A	B	C	D	
a	b	c	d
*/

#include<stdio.h>

void pattern(int iRow, int iColumn)
{
    int i  = 0 , j = 0 ;
    char ch1,ch2;

    for(i = 1; i <= iRow; i++)
    {
        for(j = 1,ch1='A',ch2='a'; j <= iColumn; j++,ch1++,ch2++)
        {
           if(i%2 == 0)
           {
           printf("%c\t",ch2);
           }
           else
           {
            printf("%c\t",ch1);

           }
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