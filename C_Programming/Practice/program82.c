#include<stdio.h>

void pattern(int iRow, int iColumn)
{
    int iCntR  = 0 , iCntC = 0 ;
    for(iCntR = 1; iCntR <= iRow; iCntR++ )
    {
        for(iCntC = 1; iCntC <= iColumn; iCntC++)
        {
            printf(" %d ",iCntC);
        }
        printf("\n");

    }
    
    printf("\n");

}
int main()
{
    int iValue1 = 0 , iValue2 = 0;

    printf("Enter number of elements:");
    scanf("%d",&iValue1);

    printf("Enter number of elements:");
    scanf("%d",&iValue2);


    pattern(iValue1, iValue2);
    return 0;
}

///////////////////////////////////////
//////
///// Input: iRow =4 iCol =3
/////    1  2  3 
/////    1  2  3 
/////    1  2  3 
/////
////////////////////////////////////////