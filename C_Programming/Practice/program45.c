#include<stdio.h>
int CountDiff(int iNo)
{
    int iDigit = 0,iDiff = 0;
   
    int iEvenSum = 0,iOddSum = 0;

        while(iNo != 0)
        {
           iDigit =  iNo % 10;
            
          if(iDigit % 2 == 0)
          {
            iEvenSum = iEvenSum +  iDigit;
        
          }
          else
          {
             iOddSum = iOddSum + iDigit;
          }

           
           iNo = iNo / 10;
        }
        
        iDigit = iEvenSum - iOddSum;

        return iDigit;
}
int main()
{
    int iValue = 0;
    int iRet = 0;

    printf("Enter number:\n");
    scanf("%d",&iValue);

    iRet = CountDiff(iValue);

    printf("%d\n",iRet);

    return 0;

}