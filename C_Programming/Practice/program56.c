#include<stdio.h>
#include<stdlib.h>

int Difference(int Arr[], int iSize)
{
    int iCnt = 0;
    int iEvenSum = 0;
    int iOddSum = 0;
    int iDiff = 0;

    for(iCnt = 0; iCnt < iSize; iCnt++)
    {
        if(Arr[iCnt] % 2 == 0)
       {
         iEvenSum = iEvenSum + Arr[iCnt];
       }
       else
       {
         iOddSum = iOddSum + Arr[iCnt];
       }
    }

    iDiff = iEvenSum - iOddSum;

    return iDiff;
}



int main()
{
  
    int *Brr = NULL;
    int iLength,iCnt = 0;
    int iRet = 0;

    printf("Enter a number of element: \n");
    scanf("%d",&iLength);

    Brr = (int *)malloc(sizeof(int) * iLength); 

    if(Brr == NULL)
    {
        printf("Unable to allocate memory ");
        return -1;
    }

    printf("Enter the elements:\n");

    for(iCnt = 0; iCnt < iLength; iCnt++)
    {
        scanf("%d",&Brr[iCnt]);
    }

    iRet = Difference(Brr , iLength);

    printf("Result is %d\n",iRet);

    free(Brr);


    return 0;
}

///////////////////////////////////
////////
//////// Enter a number of element: 
////////  4
//////// Enter the elements:
////////  1
////////  2
////////  3
////////  4
//////// Result is 2  (6 - 2)
////////////////////////////////////