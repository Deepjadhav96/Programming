class Logic
{
    void displayGrade(int iMarks)
    {
        if(iMarks >= 80)
        {
            System.out.println("Distinction");
        }
        else if( iMarks >= 70 && iMarks < 80)
        {
            System.out.println("first class");
                    
        }
        else if( iMarks >= 50 && iMarks < 70 )
        {
            System.out.println("Second class");
        }
        else if(iMarks >= 35 && iMarks < 50)
        {
            System.out.println("Pass class");
        }
        else
        {
            System.out.println("Fail");
        }
    }

}



class program12
{
    public static void main(String A[])
    {
        Logic lobj = new Logic();
        lobj.displayGrade(12);
    }
}