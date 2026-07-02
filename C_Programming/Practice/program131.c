#include<stdio.h>
#include<string.h>
void stringToLower(char str[])
{
    
    int i = 0;
    for(i = 0; i <= strlen(str); i++)
    {
        if(str[i] >= 'A' && str[i] <= 'Z')
        {
            printf("%c",((char)str[i]+32));
        }
        else
        {
            printf("%c",str[i]);
        }
    }
    printf("\n");
    

}
int main()
{
    char ch[40] = {0};
    printf("Enter a String: ");
    scanf("%[^'\n']s",ch);

    stringToLower(ch);

    return 0;
}