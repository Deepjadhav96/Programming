import os
import sys
import hashlib

def CompareFile(FileName1,FileName2):
    hobj1 = hashlib.md5()
    Buffer = FileName1.read(1024)

    while(len(Buffer) > 0):
        hobj1.update(Buffer)
        Buffer = FileName1.read(1024)
    FileName1.close()

    hobj2 = hashlib.md5()
    Buffer2 = FileName2.read(1024)

    while(len(Buffer2) > 0):
            hobj2.update(Buffer2)
            Buffer2 = FileName2.read(1024)
    FileName2.close()

    if hobj1.hexdigest() == hobj2.hexdigest():
         return True
    else:
         return False
    
def main():
    try:
        FileName1 = open(sys.argv[1],"rb")
        FileName2 = open(sys.argv[2],"rb")

        Result = CompareFile(FileName1,FileName2)
     
    except FileNotFoundError as fobj:
        print("File is not present in the current directory")


    if Result == True:
         print(f"{sys.argv[1]} and {sys.argv[2]} are both files are same")
    else:
         print(f"{sys.argv[1]} and {sys.argv[2]} are both files are different")

if __name__=="__main__":
    main()

#Incomplete 
#Learn about the CheckSum