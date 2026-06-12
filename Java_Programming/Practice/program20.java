
class Logic
{
    void findSmallestDigit(int iNo)
    {
        int iDigit = 0 , iMin = 9;
        while(iNo != 0)
        {
           iDigit = iNo % 10;
           if(iDigit < iMin)
           {
             iMin = iDigit;
           }
           iNo = iNo / 10;

        }
        System.out.println(iMin);
        
    }
}


class program20

{
    public static void main(String A[])
    {
        Logic lobj = new Logic();
        lobj.findSmallestDigit(15964);

    }
}