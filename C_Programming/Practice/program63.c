#include<stdio.h>
#include<stdlib.h>
#include<stdbool.h>

bool frequency(int Arr[], int iSize)
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

    if(iCount < iSize)
    {
        return true;
    }
    else
    {
        return false;
    }
}



int main()
{
  
    int *Brr = NULL;
    int iLength,iCnt = 0;
    bool bRet = false;

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

    bRet = frequency(Brr , iLength);

    if(bRet == true)
    {
        printf("11 is present \n");
    }
    else
    {
        printf("11 is absent \n");
    }

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
////////  11 is present
////////
////////////////////////////////////