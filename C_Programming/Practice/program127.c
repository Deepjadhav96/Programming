/*
Enter a string:MarveLLous FaMily
MARVELLOUS FAMILY
*/

#include<stdio.h>

void struprx(char *str)
{
    while (*str != '\0')
    {
        if(*str >= 97 && *str <=122 )
        {
            *str =(char)(*str - 32);
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

    struprx(Arr);
    return 0;
}