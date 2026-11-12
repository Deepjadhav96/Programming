#Count lines in file

def LineCountFile(fobj):
    counter  = 0
    for line in fobj:
        counter = counter + 1
    print("Lines in file are:",counter)

def main():
    try:
        fobj = open("Demo.txt","r")
        print("File gets opened")
    except FileNotFoundError as sobj:
        print("File is not present in the current directory")

    LineCountFile(fobj)
if __name__ == "__main__":
    main()