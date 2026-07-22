def main():
    try:
        fobj = open("Demo.txt",'r')
        Data = fobj.read()
        Data = Data.split()         #Removes the extra spaces and handles newline 
        print("Count of words are: ",len(Data))
                
    except FileNotFoundError as fobj:
        print("File is not found in the directory")
if __name__ == "__main__":
    main()