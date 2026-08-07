//Write a Java program to accept a file name from the user and open that file.
import java.util.Scanner;
import java.io.FileInputStream;


class program1
{
    public static void main(String A[])throws Exception
    {
        String str = null;
        Scanner sobj = new Scanner(System.in);
        
        System.out.println("Enter file name :");
        str = sobj.nextLine(); 

        FileInputStream fobj = new FileInputStream(str);
        System.out.println("File gets open  at this location:"+fobj);

        fobj.close();

    }
}
