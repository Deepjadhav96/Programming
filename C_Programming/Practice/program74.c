#include<stdio.h>
#include<stdlib.h>
void DigitPresent(int Arr[], int iSize)
{
    int iCnt = 0, iDigit = 0;
    

    for(iCnt = 0; iCnt < iSize; iCnt++)
    {
        while (Arr[iCnt] != 0)
        {
            iDigit = Arr[iCnt] % 10;
            if(iDigit == 3)
            {
                printf("%d \t \n",Arr[iCnt]);
            }
            Arr[iCnt] = Arr[iCnt] / 10;

        }
        
    }

    
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

     DigitPresent(Brr, iLength);

    free(Brr);


    return 0;
}