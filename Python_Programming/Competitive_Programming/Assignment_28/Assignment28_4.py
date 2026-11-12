import shutil
#Copy file content into another file
  
def CopyFile(fobj,fobj2):
    shutil.copyfileobj(fobj,fobj2)

   
       
       
def main():
    try:
        fobj = open("Demo.txt","r")
        fobj2 = open("DemoCopy.txt","w")
        print("Data copied successfully")
    except FileNotFoundError as sobj:
        print("File is not present in the current directory")

    CopyFile(fobj,fobj2)
if __name__ == "__main__":
    main()