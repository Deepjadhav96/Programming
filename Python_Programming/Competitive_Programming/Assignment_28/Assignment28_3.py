#Display file line by line 
def DisplayFile(fobj):
   # print(fobj.read())
   for lines in fobj:
       print(lines,end="")
       
       
       
def main():
    try:
        fobj = open("Demo.txt","r")
        print("File gets opened")
    except FileNotFoundError as sobj:
        print("File is not present in the current directory")

    DisplayFile(fobj)
if __name__ == "__main__":
    main()