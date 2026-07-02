#include<stdio.h>
#include<string.h>
void StringToggle(char str[])
{
    int count = 0;
    
    int i = 0;
    for(i = 0; i <= strlen(str); i++)
    {
        if(str[i]==' ')
        {
           printf("%c",str[i]);
           count++;
        }
        
    }
    printf("%d\n",count);
    

}
int main()
{
    char ch[40] = {0};
    printf("Enter a String: ");
    scanf("%[^'\n']s",ch);

    StringToggle(ch);

    return 0;
}