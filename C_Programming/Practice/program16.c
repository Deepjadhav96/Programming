#include<stdio.h>
int MultiFact(int iNo)
{
    int iCnt = 0;
    int iMulti = 1;
    for(iCnt = 1; iCnt <= iNo/2; iCnt++)
    {
        if(iNo % iCnt == 0)
        {
             iMulti = iMulti * iCnt;
             
        }
    }
    return iMulti;

}

int main()
{
    int iValue = 0;
    int iRet = 0;

    printf("Enter a number: \n");
    scanf("%d",&iValue);

    iRet = MultiFact(iValue);
    printf("%d\n",iRet);

    return 0;
}

///////////////////////////////////
///
///  Input: 12
///  Output: 144 (1 * 2 * 3 * 4 * 6)
///
///  Input: 13
///  Output: 1
///////////////////////////////////