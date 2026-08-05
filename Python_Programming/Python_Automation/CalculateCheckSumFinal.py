import sys 
import os
import hashlib

def CalCulateCheckSum(Filename):
    fobj = open(Filename,"rb")
    hobj = hashlib.md5()
    Buffer = fobj.read(1024)
   

    while(len(Buffer)>0):
        hobj.update(Buffer)
        Buffer = fobj.read(1024)
    fobj.close()
    return hobj.hexdigest
    
def main():
    Ret = CalCulateCheckSum("Demo.txt")

    print("CheckSum of file is: ",Ret)


if __name__ == "__main__":
    main()