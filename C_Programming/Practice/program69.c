#include<stdio.h>
#include<stdlib.h>
void Range(int Arr[], int iSize, int iStart,int iEnd)
{
    int iCnt = 0, iOccurence = 0;

    for(iCnt = 0; iCnt < iSize; iCnt++)
    {
        if(Arr[iCnt] >= iStart && Arr[iCnt] <= iEnd)
        {
            printf("%d\t \n",Arr[iCnt]);
            
        }
    }

    
}
int main()
{
    int iLength = 0, iCnt = 0;
    int *Brr = NULL;
    int iStart = 0;
    int iEnd = 0;
    
    
    printf("Enter number of element:\n");
    scanf("%d",&iLength);

    printf("Enter a Start of Range:");
    scanf("%d",&iStart);

    printf("Enter an End of Range:");
    scanf("%d",&iEnd);

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

     Range(Brr,iLength,iStart,iEnd);

    free(Brr);


    return 0;
}

/////////////////////////////////////////
//////// Enter a number of element: 
////////  4
///////// Enter a Start of Range:
////////  40
////////  Enter an End of Range:
////////  100
//////// Enter the elements:
////////  12
////////  6
////////  2
////////  80
////////  46
///////// 
///////// 46
///////// 80
//////////////////////////////////////////