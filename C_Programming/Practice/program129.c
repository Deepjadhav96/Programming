#include<stdio.h>

void DisplayDigit(char *str)
{
    while (*str != '\0')
    {
       if(*str >=48 && *str <= 57)
       {
         printf("%c",*str);
       }
       printf("\n");
        str++;
    }
    

}


int main()
{
    char Arr[20] = {0};

    printf("Enter a string:");
    scanf("%[^'\n']s",Arr);

    DisplayDigit(Arr);
    return 0;
}