class Logic
{
    void productofDigit(int iNo)
    {
        int iDigit = 0;
        int iProduct = 1;
        for(;iNo != 0;)
        {
            iDigit = iNo % 10;
            iProduct = iProduct * iDigit;
            iNo = iNo / 10;
        }
        System.out.println(iProduct);
    }
}
class program21
{
    public static void main(String A[])
    {
        Logic lobj = new Logic();
        lobj.productofDigit(234);
    }
}