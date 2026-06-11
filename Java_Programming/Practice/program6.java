class Logic
{
    void CheckPrime(int iNum)
    {
        int iCnt = 0 , iTemp = 0;

        for(iCnt = 2; iCnt < iNum/2; iCnt++)
        {
             if(iNum % iCnt == 0)
            {
                iTemp++;
            }
        }
        if(iTemp >= 2)
        {
            System.out.println("It is not prime number");
        }
        else
        {
            System.out.println("It is prime number");
        }

    }
}


class program6
{
    public static void main(String A[])
    {
        Logic lobj = new Logic();
        lobj.CheckPrime(11);

    }
}