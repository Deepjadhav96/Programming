class Logic
{
    void printEvenNumbers(int iNum)
    {
        int iCnt = 0;
        for(iCnt = 1; iCnt < iNum; iCnt++)
        {
            if(iCnt % 2 == 0 )
            {
                System.out.println(iCnt);
            }
        }
    }
}


class program7
{
    public static void main(String A[])
    {
        Logic lobj = new Logic();
        lobj.printEvenNumbers(11);

    }
}