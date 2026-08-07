//2. Write a Java program to accept a file name from the user, open that file, and display the contents on the screen.
import java.util.Scanner;
import java.io.*;

class FileDisplayInfo 
{
    void Display() throws Exception
    {
        String str = null;
        Scanner sobj = new Scanner(System.in);
        int data =0;
        
        System.out.println("Enter file name :");
        str = sobj.nextLine(); 

        FileInputStream fobj = new FileInputStream(str);

        // BufferInputStream bobj = new BufferInputStream(fobj);

        System.out.println("Content from file: ");

        while((data = fobj.read())!=-1)
        {
          System.out.println((char)data);
        }


    }

}

class program2
{
    public static void main(String A[]) throws Exception
    {
        FileDisplayInfo fobj = new FileDisplayInfo();
        fobj.Display();

    }
}