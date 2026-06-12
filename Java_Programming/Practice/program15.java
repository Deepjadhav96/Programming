class Logic
{
    void calculatePower(int base , int exp)
    {
        int iCnt = 0, iPower = 1;
        for(iCnt = 1; iCnt <= exp; iCnt++)
        {
            iPower = iPower * base;
        }
        System.out.println(iPower);
        
    }
}


class program15
{
    public static void main(String A[])
    {
        Logic lobj = new Logic();
        lobj.calculatePower(2 , 5);

    }
}