#include<stdio.h>
#include<stdlib.h>
int Product(int Arr[], int iSize)
{
    int iCnt = 0, iOccurence = 0;
    int iOddMult = 1;

    for(iCnt = 0; iCnt < iSize; iCnt++)
    {
        if(Arr[iCnt] % 2 != 0)
        {
            iOddMult = iOddMult * Arr[iCnt];
        }
    }

    return iOddMult;
    
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

     iRet = Product(Brr, iLength);
     printf("Multiplication of ODD elements: %d\n",iRet);

    free(Brr);


    return 0;
}

///////////////////////////////////////
//////// Enter a number of element: 
////////  6
//////// Enter the elements:
////////  15
////////  66
////////  3
////////  70
////////  10
///////// 88
/////////Output:
///////// 45
//////////////////////////////////////////