#include<stdio.h>
#include<stdlib.h>
#include<stdbool.h>

int frequency11(int Arr[], int iSize)
{
   int iCnt = 0;
   int iCount = 0;

    for(iCnt = 0; iCnt < iSize; iCnt++)
    {
       if(Arr[iCnt] == 11)
       {
         iCount++;
       }
    }
  
    return iCount;
}



int main()
{
  
    int *Brr = NULL;
    int iLength,iCnt = 0;
    int iRet = false;

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

    iRet = frequency11(Brr , iLength);

    printf("frequency of 11 is: %d \n",iRet);

    free(Brr);


    return 0;
}

///////////////////////////////////
////////
//////// Enter a number of element: 
////////  5
//////// Enter the elements:
////////  11
////////  66
////////  11
////////  2
////////  1
////////  frequency of 11 is: 2
////////
////////////////////////////////////