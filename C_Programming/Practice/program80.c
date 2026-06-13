#include<stdio.h>

void pattern(int iNo)
{
    int iCnt = 0;
    for(iCnt = 2; iCnt <= (iNo*2); iCnt = iCnt + 2)
    {
        printf(" %d ",iCnt);
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
//////////////////////////////
///
/// Input:  8
/// Output:  2  4  6  8  10  12  14  16
///
////////////////////////////////
 