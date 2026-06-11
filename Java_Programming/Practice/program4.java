class Logic
{
    void findMax(int iNo1, int iNo2, int iNo3)
    {
        if(iNo1 > iNo2 && iNo1 > iNo3)
        {
            System.out.println("Max number is: "+iNo1);
        }
        else if( iNo2 > iNo1 && iNo2 > iNo3)
        {
            System.out.println("Max number is :"+iNo2);
        }
        else
        {
            System.out.println("Max number is "+iNo3);
        }
    }

}

class program4
{
    public static void main( )
    {
            Logic lobj = new Logic();
            lobj.findMax(11,21,41);
    }
}