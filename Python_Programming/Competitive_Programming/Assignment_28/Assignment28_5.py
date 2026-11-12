#Check the word is present in the file or not.
def CheckWord(fobj,word):
    counter  = 0
    Data = fobj.read()
    if (Data.find(word,0)==True):
        print(f"{word} is present in the file")
    else:
        print(f"{word} is not present in the file")
        
def main():
    try:
        fobj = open("Demo.txt","r")
        print("File gets opened")
    except FileNotFoundError as sobj:
        print("File is not present in the current directory")
    word = input("Enter a word: ")
    CheckWord(fobj,word)
if __name__ == "__main__":
    main()