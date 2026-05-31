#include<stdio.h>


void FactRev(int iNo)
{
    if(iNo <= 0)
    { 
        return;
    }

    int iCnt = 0;
    for(iCnt = iNo/2; iCnt >= 1; iCnt--)
    {
        iNo % iCnt;
        printf("%d \t",iCnt);

    }

    printf("\n");   

}

int main()
{
    int iValue = 0;

    printf("Enter a value:\n");
    scanf("%d",&iValue);

    FactRev(iValue);

    return 0;
}

///////////////////////////////////
///
///  Input: 12
///  Output: 6 4 3 2 1
///
///  Input: 13
///  Output: 1
///////////////////////////////////




















///////////////////////
///
///  Input: 12
///  output: 6 4 3 2 1
///
///  Input: 10
///  Output: 5 2 1
///
///
///////////////////////////