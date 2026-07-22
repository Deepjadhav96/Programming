import sys
def main():
    try:
        fobj = open("Demo.txt",'r')
        Data = fobj.read()
        
        if sys.argv[1] in Data:
                print(sys.argv[1],"is present in file")

    except FileNotFoundError as fobj:
        print("File is not found in the directory")
if __name__ == "__main__":
    main()