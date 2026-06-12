class Logic
{
    void sumEvenOddDigits(int iNum)
    {
        int  iDigit = 0;
        int iSumOdd = 0, iSumEven = 0;

       while(iNum != 0)
        {   
             iDigit = iNum % 10;

            if(iDigit % 2 != 0 )
            {
                iSumOdd = iSumOdd + iDigit;
            }
            else
            {
                iSumEven = iSumEven + iDigit;
            }
            iNum = iNum / 10;
        }
        System.out.println("Sum of odd digits :"+iSumOdd);
        System.out.println("Sum of even digits :"+iSumEven);
    }
}


class program9
{
    public static void main(String A[])
    {
        Logic lobj = new Logic();
        lobj.sumEvenOddDigits(1344);

    }
}