class Logic
{
    boolean checkDivisible(int iNo)
    {
        if(iNo % 5 == 0 && iNo % 11 == 0 )
        {
            return  true;
        }
        else
        {
            return false;
        }
        
    }

}



class program13
{
    public static void main(String A[])
    {
        boolean iRet = false;
        Logic lobj = new Logic();
        iRet = lobj.checkDivisible(55);

        if(iRet == true)
        {
            System.out.println("Divisible by 5 and 11");
        }
        else
        {
            System.out.println("Not divisible by 5 and 11");
        }
    }
}