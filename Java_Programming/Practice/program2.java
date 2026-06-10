class Logic
{
    void CheckPalindrome(int iNum)
    {
        int iCnt = 0;
        int iDigit = 0, iSum = 0;
        int iRev = 0, iTemp = 0;
        iTemp = iNum;

        while(iNum != 0)
        {
            iDigit = iNum % 10;
           
            iRev = (iRev * 10) + iDigit;

            iNum = iNum / 10;

        }

        if(iTemp == iRev)
        {
            System.out.println("Number is palindrome");
        }
        else
        {
            System.out.println("Number is not palindrome");
        }

    }
}


class program2X
{
    public static void main(String A[])
    {
        Logic lobj = new Logic();
        lobj.CheckPalindrome(121);

    }
}