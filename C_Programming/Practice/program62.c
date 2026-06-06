#include<stdio.h>
#include<stdlib.h>

int frequency(int Arr[], int iSize)
{
    int iCnt = 0;
    int iOddCount = 0, iEvenCount = 0;
    int iDiff = 0;
    
    for(iCnt = 0; iCnt < iSize; iCnt++)
    {
       if(Arr[iCnt] % 2 == 0)
       {
            iEvenCount++;
       }
       else
       {
            iOddCount++;
       }
    }

    iDiff = iEvenCount- iOddCount;

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

    iRet = frequency(Brr , iLength);

    printf("Difference of frequency even and odd number:%d\n",iRet);

    free(Brr);


    return 0;
}

///////////////////////////////////
////////
//////// Enter a number of element: 
////////  7
//////// Enter the elements:
////////  85
////////  66
////////  3
////////  80
////////  93
////////  88
//////// Difference of frequency even and odd number: 1 (4 - 3)
//////// 
////////////////////////////////////