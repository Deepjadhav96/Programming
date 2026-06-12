class Logic
{
    void countFactors(int iNo)
    {
       int iCnt = 0,iCount = 0;

        for(iCnt = 1; iCnt <= iNo/2; iCnt++)
        {
            if(iNo % iCnt == 0)
            {
                iCount++;
            }
        }
        System.out.println(iCount);
        
    }
}
class program24
{
    public static void main(String A[])
    {
        Logic lobj = new Logic();
        lobj.countFactors(4);
    }
}