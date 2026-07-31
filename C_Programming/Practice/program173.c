#include<stdio.h>
#include<string.h>
#include<fcntl.h>
#include<unistd.h>
#include<sys/stat.h>

#define BSIZE 1024

void Display(char *fileName)
{
    char Buffer[BSIZE] = {'\0'};
    int fd = 0, iRet = 0;
    fd = open(fileName,O_RDONLY);

    if(fd == -1 )
    {
        printf("Unable to open file \n");
    }
    else
    {
        while ((iRet = read(fd,Buffer,sizeof(Buffer))) != 0)
        {
            write(1,Buffer,sizeof(Buffer));
            memset(Buffer,'\0',sizeof(Buffer));
        }
    }

}


int main()
{
    char fName[30] ={'\0'}; 

    printf("Enter a file name :");
    scanf("%[^'\n']s",fName);

    Display(fName);

    return 0;
}