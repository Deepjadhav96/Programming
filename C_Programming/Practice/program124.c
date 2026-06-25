#include<stdio.h>
#include<stdbool.h>


bool ChkVowel(char *ch)
{
   while(ch != '\0')
   {
        if(ch == 'A' || ch == 'a' || ch == 'E' || ch == 'e' 
        || ch == 'I' || ch == 'i' || ch == 'O' || ch =='o' || 
        ch == 'U' || ch == 'u')
        {
            return true;
        }
        else
        {
            return false;
        }
   }

}

int main()
{
    char cArr[20] = {'\0'};
    bool bRet = false;

    printf("Enter a string:");
    scanf("%[^'\n']s",cArr);

    bRet = ChkVowel(cArr);

    if(bRet == true)
    {
        printf("Vowels is present..");
    }
    else
    {
        printf("Vowels is present..");
    }
  
    return 0;
}