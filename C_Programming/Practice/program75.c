#include<stdio.h>
#include<stdlib.h>
void DigitsSum(int Arr[], int iSize)
{
    int iCnt = 0, iDigit = 0, iSum = 0;
    

    for(iCnt = 0; iCnt < iSize; iCnt++)
    {
        while (Arr[iCnt] != 0)
        {
            iDigit = Arr[iCnt] % 10;
            iSum = iSum + iDigit;
            Arr[iCnt] = Arr[iCnt] / 10;

        }
        printf("%d\t \n",iSum);
         iSum = 0;
          
    }
   

    
}
int main()
{
    int iLength = 0, iCnt = 0 , iRet = 0;
    int *Brr = NULL;
    
    
    printf("Enter number of element:\n");
    scanf("%d",&iLength);



    Brr = (int *)malloc(sizeof(int) * iLength);

    if(Brr == NULL)
    {
        printf("Unable to allocate the memory");
        return -1;
    }

    printf("Enter an elements:\n");
    for(iCnt = 0; iCnt < iLength; iCnt++)
    {
        scanf("%d",&Brr[iCnt]);
    }

     DigitsSum(Brr, iLength);

    free(Brr);


    return 0;
}