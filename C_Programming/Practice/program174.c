#include<stdio.h>
#include<string.h>
#include<fcntl.h>
#include<unistd.h>
#include<sys/stat.h>


void DisplaySize(char *fileName)
{
    struct stat sobj;
    stat(fileName, &sobj);
    printf("Size of files in bytes are: %ld\n",sobj.st_size);
}

int main()
{
    char fName[30] ={'\0'}; 
    int iRet = 0;

    printf("Enter a file name :");
    scanf("%[^'\n']s",fName);

    DisplaySize(fName);

    return 0;
}