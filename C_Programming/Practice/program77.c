#include<stdio.h>

void pattern(int iNo)
{
    int iCnt = 0;
    for(iCnt = iNo; iCnt > 0; iCnt--)
    {
        printf(" %d #",iCnt);
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
/// Output:  5 # 4 # 3 # 2 # 1 #
///
///////////////////////