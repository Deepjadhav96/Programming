#include<stdio.h>
#include<string.h>
void StringToggle(char str[])
{
    
    int i = 0;
    for(i = 0; i <= strlen(str); i++)
    {
        if(str[i] >= 'a' && str[i] <= 'z')
        {
            printf("%c",((char)str[i]-32));
        }
        else if(str[i] >= 'A' && str[i] <= 'Z')
        {
           printf("%c",((char)str[i]+32));
        }
        else
        {
            printf("%c",((char)str[i]));
        }
    }
    printf("\n");
    

}
int main()
{
    char ch[40] = {0};
    printf("Enter a String: ");
    scanf("%[^'\n']s",ch);

    StringToggle(ch);

    return 0;
}