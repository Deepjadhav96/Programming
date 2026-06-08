#include<stdio.h>
#include<stdlib.h>
int Difference(int Arr[], int iSize)
{
    int iCnt = 0,iDiff = 0;
    int iMin = Arr[iCnt];
    int iMax = Arr[iCnt];

    for(iCnt = 0; iCnt < iSize; iCnt++)
    {
        if(Arr[iCnt] < iMin)
        {
            iMin = Arr[iCnt];
        }
        if(Arr[iCnt] > iMax)
        {
            iMax = Arr[iCnt];
        }
    }

    iDiff = iMax - iMin;

    return iDiff;
    
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

     iRet = Difference(Brr, iLength);
     printf("Difference of number is : %d\n",iRet);

    free(Brr);


    return 0;
}

///////////////////////////////////////
//////// Enter a number of element: 
////////  6
//////// Enter the elements:
////////  85
////////  66
////////  3
////////  66
////////  93
////////  88
///////// Output:
///////// 90 (93-3)
//////////////////////////////////////////