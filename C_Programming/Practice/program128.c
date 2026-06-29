#include<stdio.h>

void strtogglex(char *str)
{
    while (*str != '\0')
    {
        if(*str >= 97 && *str <=122 )
        {
            *str =(char)(*str - 32);
        }
        else
        {
            *str =(char)(*str + 32);
        }
        printf("%c\n",*str);
        str++;
    }
    

}


int main()
{
    char Arr[20] = {0};

    printf("Enter a string:");
    scanf("%[^'\n']s",Arr);

    strtogglex(Arr);
    return 0;
}