/*
Accept division of student from user and depends on the division display exam timing . 
There are four Divisions in school as A,B,C,D.
Exam of division A at 7 AM, B at 8.30 AM, C at 9.20AM 
and D at 10.30 AM.
(Application should case sensitive)
*/

#include<stdio.h>

void DisplaySchedule(char cDiv)
{
    if(cDiv != 'A' && cDiv != 'B' && cDiv != 'C' && cDiv != 'D')
    {
        printf("Enter your Division correctly....!\n");
        return;
    }

    else
     {    if(cDiv == 'A')
        {
            printf("Your exam time at 7AM\n");
        }
        else if (cDiv == 'B')
        {
            printf("Your exam time at 8.30 AM\n");
          
        }
        else if (cDiv == 'C')
        {
            printf("Your exam time at 9.20 AM\n");            
        }
        else
        {
            printf("Your exam time at 10.30AM\n");

        }
     }
    

}
int main()
{
    char cValue = '\0';

    printf("--------------------------------------------------------------\n");
    printf("---------------Exam Scheduler Application---------------------\n");
    printf("--------------------------------------------------------------\n");

    printf("Enter your Division to check exam time :");
    scanf("%c",&cValue);

    DisplaySchedule(cValue);

    return 0;
}
