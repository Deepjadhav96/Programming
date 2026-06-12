class Logic
{
    void printDivisibleBy2and3(int iNo)
    {
       int iCnt = 0, iCount = 0;

        for(iCnt = 1; iCnt <= iNo; iCnt++)
        {
            if(iCnt % 2 == 0 && iCnt % 3 == 0)
            {
                iCount++;
            }
        }
        System.out.println(iCount);
        
    }
}
class program25
{
    public static void main(String A[])
    {
        Logic lobj = new Logic();
        lobj.printDivisibleBy2and3(20);
    }
}