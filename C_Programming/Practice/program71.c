#include<stdio.h>
#include<stdlib.h>
int Maximum(int Arr[], int iSize)
{
    int iCnt = 0;
    int iMax = Arr[iCnt];

    for(iCnt = 0; iCnt < iSize; iCnt++)
    {
        if(Arr[iCnt] > iMax)
        {
            iMax = Arr[iCnt];
        }
    }

    return iMax;
    
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

     iRet = Maximum(Brr, iLength);
     printf("Maximum number is : %d\n",iRet);

    free(Brr);


    return 0;
}

///////////////////////////////////////
//////// Enter a number of element: 
////////  4
//////// Enter the elements:
////////  123
////////  -6
////////  35
////////  895
////////  123
///////// Output:
///////// 895
//////////////////////////////////////////