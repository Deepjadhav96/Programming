#include<stdio.h>
#include<string.h>
#include<fcntl.h>
#include<unistd.h>
#include<sys/stat.h>

void creatFile(char *fileName)
{
    int fd = 0;
    fd = creat(fileName,O_RDONLY | O_RDWR);
    if(fd == -1 )
    {
        printf("Unable to create file \n");
    }
    else
    {
        printf("File created successfully\n");
    }

}


int main()
{
    char fName[30] ={'\0'}; 

    printf("Enter a file name :");
    scanf("%[^'\n']s",fName);

    creatFile(fName);

    return 0;
}