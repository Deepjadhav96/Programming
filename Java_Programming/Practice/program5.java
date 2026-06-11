class Logic
{
    void table(int iNo)
    {
        int iCnt = 0 , iTable = 0;

        for(iCnt = 1; iCnt <= 10; iCnt++)
        {
            iTable = iNo * iCnt;
            System.out.println(iTable);
        }
    }

}

class program5
{
    public static void main( )
    {
            Logic lobj = new Logic();
            lobj.table(11);
    }
}