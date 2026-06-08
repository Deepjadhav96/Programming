#include<stdio.h>
#include<stdlib.h>
int FirstOcc(int Arr[], int iSize, int iNo)
{
    int iCnt = 0, iOccurence = 0;

    for(iCnt = 0; iCnt < iSize; iCnt++)
    {
        if(Arr[iCnt] == iNo)
        {
            iOccurence = iCnt;
            break;
        }
    }

    return iOccurence;
}
int main()
{
    int iLength = 0, iCnt = 0;
    int *Brr = NULL;
    int iValue = 0;
    int iRet = 0;
    
    printf("Enter number of element:\n");
    scanf("%d",&iLength);

    printf("Enter a number:");
    scanf("%d",&iValue);

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

    iRet = FirstOcc(Brr,iLength,iValue);
    printf("First occurence of an element is at index:%d\n",iRet);

    free(Brr);


    return 0;
}

/////////////////////////////////////////
//////// Enter a number of element: 
////////  5
///////// Enter a number: 
////////  46
//////// Enter the elements:
////////  12
////////  6
////////  2
////////  80
////////  46
///////// First occurence of an element is at index: 4
//////////////////////////////////////////