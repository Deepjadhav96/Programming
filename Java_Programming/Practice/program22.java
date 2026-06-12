class Logic
{
    void countEvenOddRange(int iNo)
    {
        int iCnt = 0, iCountEven = 0, iCountOdd = 0;
        for(iCnt = 1; iCnt <= iNo; iCnt++)
        {
            if(iCnt % 2 == 0)
            {
                iCountEven++;
            }
            else
            {
                iCountOdd++;
            }
        }
        System.out.println("Count of even numbers are: "+iCountEven);
        System.out.println("Count of odd number are : "+iCountOdd);
        
    }
}
class program22
{
    public static void main(String A[])
    {
        Logic lobj = new Logic();
        lobj.countEvenOddRange(4);
    }
}