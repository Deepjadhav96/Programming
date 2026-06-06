#include<stdio.h>
#include<stdlib.h>

void Display(int Arr[], int iSize)
{
    int iCnt = 0;

    printf("This numbers are divisible by 5 : \n");

    for(iCnt = 0; iCnt < iSize; iCnt++)
    {
        if(Arr[iCnt] % 5 == 0)
        {
          printf("%d \n",Arr[iCnt]);
        }
        
    }

    
}
int main()
{
  
    int *Brr = NULL;
    int iLength,iCnt = 0;


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

    
    Display(Brr , iLength);

    free(Brr);


    return 0;
}

///////////////////////////////////
////////
//////// Enter a number of element: 
////////  3
//////// Enter the elements:
////////  5
////////  15
////////  1
////////  This numbers are divisible by 5 :
////////  5
////////  15
////////////////////////////////////