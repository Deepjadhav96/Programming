class Logic
{
    void checkLeapYear(int year)
    {
        if(year % 4 == 0)
        {
            System.out.println("Leap year");
        }
        else
        {
            System.out.println("Not leap year");
                    
        }
    }

}



class program11
{
    public static void main(String A[])
    {
        Logic lobj = new Logic();
        lobj.checkLeapYear(2024);
    }
}