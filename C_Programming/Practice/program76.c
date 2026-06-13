#include<stdio.h>

void pattern(int iNo)
{
    int iCnt = 0;
    char ch = 'A';
    for(iCnt = 1; iCnt <= iNo; iCnt++)
    {
        printf(" %c ",ch);
        ch++;
    }
    printf("\n");
}
int main()
{
    int iValue = 0;

    printf("Enter number of elements:");
    scanf("%d",&iValue);

    pattern(iValue);
    return 0;
}

///////////////////////
///
/// Input:  5
/// Output: A B C D E
///
///////////////////////