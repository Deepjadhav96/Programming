import os
import sys
def DisplayFileContent(FileName):
    Data = FileName.read()
    print(Data)

def main():
    FileName = open(sys.argv[1],"r")

    DisplayFileContent(FileName)
    FileName.close()
if __name__=="__main__":
    main()