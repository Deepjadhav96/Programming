class Logic
{
    void checkSign(int iNum)
    {
       if(iNum > 0)
       {
        System.out.println("Positive");
       }
       else if(iNum < 0)
       {
        System.out.println("Negative");
       }
       else
       {
        System.out.println("Zero");
       }
    }
}


class program10
{
    public static void main(String A[])
    {
        Logic lobj = new Logic();
        lobj.checkSign(0);

    }
}