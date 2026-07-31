#include<stdio.h>
#include<string.h>
#include<fcntl.h>
#include<unistd.h>
void openFile(char *fileName)
{
    int fd = 0;
    fd = open(fileName,O_RDONLY);
    if(fd == -1 )
    {
        printf("Unable to find file \n");
    }
    else
    {
        printf("File opened successfully\n");
    }

}


int main()
{
    char fName[30] ={'\0'}; 

    printf("Enter a file name :");
    scanf("%[^'\n']s",fName);

    openFile(fName);

    return 0;
}