#include<stdio.h>

#define TRUE 1
#define FALSE 0
typedef int BOOL;


BOOL ChkZero(int iNo)
{
    int iDigit = 0;
   while(iNo != 0)
    {
       iDigit =  iNo % 10;
       if(iDigit == 0)
       {
        return TRUE;
       }
       else
       {
        return FALSE;
       }
       iNo = iNo / 10;
    }


}
int main()
{  
    int iValue = 0;
    int iRet = 0;
    printf("Enter a number: ");
    scanf("%d",&iValue);

    iRet = ChkZero(iValue);

    if(iRet == TRUE)
    {
        printf("It contains zero \n");
    }
    else
    {

        printf("There is no zero \n");

    }
    
    return 0;
}