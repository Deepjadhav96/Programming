
class Logic
{
    void checkPerfect(int iNo)
    {
        int iCnt = 0 ,iSum = 0;
        for(iCnt = 1; iCnt <= iNo/2; iCnt++)
        {
            if( iNo % iCnt == 0)
            {
                iSum = iSum + iCnt;
            }
        }
        if(iNo == iSum)
        {
          System.out.println("Perfect number");
        }
        else
        {
            System.out.println("Not perfect number");
        }

    }
}


class program18
{
    public static void main(String A[])
    {
        Logic lobj = new Logic();
        lobj.checkPerfect(28);

    }
}