class Logic
{
    void sumOfDigits(int iNum)
    {
        int iCnt = 0;
        int iDigit = 0, iSum = 0;
        
        while(iNum != 0)
        {
            iDigit = iNum % 10;
            iSum = iSum + iDigit;
            iNum = iNum / 10;

        }
        System.out.println("Sum of digit of number:"+iSum);
    }
}


class program1
{
    public static void main(String A[])
    {
        Logic lobj = new Logic();
        lobj.sumOfDigits(1234);

    }
}