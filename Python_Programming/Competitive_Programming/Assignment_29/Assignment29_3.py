import os
import sys
import shutil

def CopyFileContent(FileName1,FileName2):
    shutil.copyfileobj(FileName1,FileName2)
    print("File content copied successfully")
   

def main():
    try:
        FileName1 = open(sys.argv[1],"r")
       
    except FileNotFoundError as fobj:
        print("File is not present in the current directory")

    FileName2 = open(sys.argv[2],"w")
    CopyFileContent(FileName1,FileName2)
if __name__=="__main__":
    main()