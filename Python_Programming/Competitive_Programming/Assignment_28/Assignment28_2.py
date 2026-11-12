#Count Word in file

def CountWords(fobj):
    counter  = 0
    for line in fobj:
        for word in line.split():
             counter = counter + 1
    print("Word in file are:",counter)

def main():
    try:
        fobj = open("Demo.txt","r")
        print("File gets opened")
    except FileNotFoundError as sobj:
        print("File is not present in the current directory")

    CountWords(fobj)
if __name__ == "__main__":
    main()