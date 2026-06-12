class Logic
{
    void sumEvenNumbers(int iNo)
    {
        int iCnt = 0, iSum = 0;
        for(iCnt = 0; iCnt < iNo; iCnt++)
        {
            if(iCnt % 2 == 0)
            {
                iSum = iSum + iCnt;
            }
        }
        System.out.println(iSum);
        
    }
}


class program16
{
    public static void main(String A[])
    {
        Logic lobj = new Logic();
        lobj.sumEvenNumbers(10);

    }
}