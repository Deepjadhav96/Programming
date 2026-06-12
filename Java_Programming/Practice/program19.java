
class Logic
{
    void findLargestDigit(int iNo)
    {
        int iDigit = 0 , iMax = 0;
        while(iNo != 0)
        {
           iDigit = iNo % 10;
           if(iDigit > iMax)
           {
             iMax = iDigit;
           }
           iNo = iNo / 10;

        }
        System.out.println(iMax);
        
    }
}


class program19
{
    public static void main(String A[])
    {
        Logic lobj = new Logic();
        lobj.findLargestDigit(15964);

    }
}