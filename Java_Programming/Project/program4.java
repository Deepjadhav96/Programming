//4. Write a Java program to accept a file name from the user and create a new file with that name if it does not exist.
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

        File fl = new File(str);

        // System.out.println("Enter a data that you want: ");
        // str2 = sobj.nextLine();

        if(fl.exists())
        {
            System.out.println("File created:");
        }
        else
        {
            FileOutputStream fobj = new FileOutputStream(fl ,true);

        }

    }

}

class program4
{
    public static void main(String A[]) throws Exception
    {
        FileDisplayInfo fobj = new FileDisplayInfo();
        fobj.Display();

    }
}
//Makes changes