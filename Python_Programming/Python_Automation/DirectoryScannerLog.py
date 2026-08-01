import sys
import os

def DirectoryScanner(DirectoryPath):
    print("Files from the directory are: ")

    fobj = open("MarvellousLog.txt","w")

    fobj.write("Marvellous Automation Scrpit\n")

    fobj.write("Files from directory are :\n")

    for FolderName, SubFolder, FileName in os.walk(DirectoryPath):
        for fname in FileName:
            fobj.write(fname+"\n")
   
    fobj.close()

def main():

    Border = "-"*80
    print(Border)
    print("Marvellous Automation Scrpit")
    print(Border)

    if ((len(sys.argv)) == 2 ):

        if(sys.argv[1]=="--h" or sys.argv[1]=="--H"):
            print("This automation scrpit is used to travel the directory")
            print("For better usage please check --u flag")
        elif(sys.argv[1]=="--u" or sys.argv[1]=="--U"):
            print("Please execute the scrpit as ")
            print("Python FileName.py DirectoryName")
            print("DirectoryName should be absolute path")
        else:
            DirectoryScanner(sys.argv[1])
            
    

    print(Border)
    print("Thank you for using Marvellous Automation Scrpit")
    print(Border)

if __name__ == "__main__":
    main()

#Basic layout of Automation scrpit