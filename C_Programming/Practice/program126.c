/*
Enter a string:MarveLLous FaMilY
marvellous family

*/
#include<stdio.h>

void strlwrx(char *str)
{
    while (*str != '\0')
    {
        if(*str >= 65 && *str <=90 )
        {
            *str =(char)(*str + 32);
        }
        printf("%c",*str);
        str++;
    }
    printf("\n");
    
    
}


int main()
{
    char Arr[20] = {0};

    printf("Enter a string:");
    scanf("%[^'\n']s",Arr);

    strlwrx(Arr);
    return 0;
}