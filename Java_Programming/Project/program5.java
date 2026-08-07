//5. Write a Java program to accept a directory name fromm the user and display the names of all files in that directory.
import java.util.Scanner;
import java.io.*;

class FileDisplayInfo 
{
    void Display() throws Exception
    {
        String str, str2 = null;
        Scanner sobj = new Scanner(System.in);

        int data =0;
        byte buffer[]; 

        
        System.out.println("Enter file name :");
        str = sobj.nextLine(); 

        

        if(str.isDirectory())
        {
            File flobj = new File();

        }
        else
        {
            System.out.println("Its not a Directory");

        }

    }

}

class program5
{
    public static void main(String A[]) throws Exception
    {
        FileDisplayInfo fobj = new FileDisplayInfo();
        fobj.Display();

    }
}