def main():
    try:
        fobj = open("Demo.txt",'r')
        print("Count of lines in file : ",len(fobj.readlines()))
    except FileNotFoundError as fobj:
        print("File is not found in the directory")
if __name__ == "__main__":
    main()