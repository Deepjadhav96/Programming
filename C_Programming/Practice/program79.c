#include<stdio.h>

void pattern(int iNo)
{
    int iCnt = 0;
    for(iCnt = 1; iCnt <= iNo; iCnt++)
    {
        printf(" #  %d  * ",iCnt);
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

//////////////////////
///
/// Input:  4
/// Output: #  1  *  #  2  *  #  3  *  #  4  * 
///
///////////////////////

 
