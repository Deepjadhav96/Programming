//3. Write a Java program to accept a file name from the user, open that file in write mode, and write some data at the end of the file.
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

        System.out.println("Enter a data that you want: ");
        str2 = sobj.nextLine();

        FileOutputStream fobj = new FileOutputStream(str ,true);
        buffer = str2.getBytes();

        fobj.write(buffer, 0, buffer.length);   
        fobj.close();    

    }

}

class program3
{
    public static void main(String A[]) throws Exception
    {
        FileDisplayInfo fobj = new FileDisplayInfo();
        fobj.Display();

    }
}