class Logic
{
    void printDigits(int iNo)
    {
        int iDigit = 0; 
        while(iNo != 0)
        {
            iDigit = iNo % 10;
            System.out.println(iDigit);
            iNo = iNo / 10;
        }
    }

}



class program14
{
    public static void main(String A[])
    {
        Logic lobj = new Logic();
        lobj.printDigits(12);
    }
}