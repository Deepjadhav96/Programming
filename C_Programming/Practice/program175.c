#include<stdio.h>
#include<string.h>
#include<fcntl.h>
#include<unistd.h>
#include<sys/stat.h>


void DisplaySize(char fileName[], char Data[])
{
    int fd = 0;
    fd = open(fileName, O_APPEND | O_RDWR);

    if(fd == -1)
    {
        printf("Unable to open file \n");
    }
    else
    {
        write(fd,Data,strlen(Data));
        printf("Data written successfully..\n");
        close(fd);
    }

}

int main()
{
    char fName[30] ={'\0'}; 
    char data[1024] ={'\0'}; 

    int iRet = 0;

    printf("Enter a file name :");
    scanf("%[^'\n']s",fName);

    printf("Enter a data :");
    scanf(" %[^'\n']s",data);

    DisplaySize(fName,data);

    return 0;
}