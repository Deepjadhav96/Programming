#include<stdio.h>
#include<stdlib.h>
#include<stdbool.h>

bool Chek(int Arr[], int iSize, int iNo)
{
   int iCnt = 0;
   int iCount = 0;

    for(iCnt = 0; iCnt < iSize; iCnt++)
    {
       if(Arr[iCnt] == iNo)
       {
         iCount++;
       }
    }

    if(iCount ==  iSize)
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
    int iRet = false;
    int iNo = 0;

    printf("Enter a number of element: \n");
    scanf("%d",&iLength);

    printf("Enter a number: \n");
    scanf("%d",&iNo);


    

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

    iRet = Chek(Brr , iLength, iNo);

   if(iRet == true)
   {
    printf("TRUE \n");
   }
   else
   {
    printf("FALSE \n");
   }

    free(Brr);


    return 0;
}

/////////////////////////////////////////
//////// Enter a number of element: 
////////  7
///////// Enter a number: 
////////  80
//////// Enter the elements:
////////  80
////////  66
////////  3
////////  80
////////  93
////////  88
///////// TRUE  (80 is present)
//////////////////////////////////////////