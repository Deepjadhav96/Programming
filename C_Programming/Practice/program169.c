//Count Spaces characters from file
#include<stdio.h>
#include<unistd.h>
#include<fcntl.h>
#include<string.h>

#define BUFFER_SIZE 1024
#define ERR_OPEN -1

int CountChar(char FileName[] , char ch)
{
    char Buffer[BUFFER_SIZE] = {'\0'}; 
    int fd = 0 , iRet = 0 ,iCount = 0, i = 0;

    fd = open(FileName,O_RDONLY);

    if(fd == -1)
    {
        return ERR_OPEN;
    }
    
    
    while ((iRet = read(fd,Buffer,sizeof(Buffer))) != 0)
    {
        for(i = 0 ; i < sizeof(Buffer); i++)
        {
            if(Buffer[i] == ch)
            {
                iCount = iCount + 1;
            }
        }
        memset(Buffer, '\0', sizeof(Buffer));           

    }

    close(fd);
    return iCount;
    
}


int main()
{
    char Fname[30] = {'\0'};
    int iRet = 0;
    char chValue = '\0';

    printf("Enter a file name: \n");
    scanf("%[^'\n']s",Fname);

    printf("Enter a character :\n");
    scanf(" %c",&chValue);

    iRet = CountChar(Fname, chValue);
    if(iRet == -1)
    {
        printf("Unable to open file\n");
    }
    else
    {
        printf("Count of character %c inside file are :%d\n",chValue,iRet);
    }

    return 0;
}