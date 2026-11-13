import os
import sys

def main():
    FileName = sys.argv[1]
    
    if (os.path.exists(FileName)==True):
        print(f"{FileName} is present in the Directory")
    else:
        print(f"{FileName} is not present in the Directory")




if __name__=="__main__":
    main()