import sys
def main():
    try:
        fobj = open("Demo.txt",'r')
        Data = fobj.read()
        
        print(Data)

    except FileNotFoundError as fobj:
        print("File is not found in the directory")
if __name__ == "__main__":
    main()