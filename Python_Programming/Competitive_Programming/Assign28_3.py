def main():
    try:
        fobj = open("Description.txt",'r')
        Data = fobj.read()
        print(Data)
        fobj.close()

    except FileNotFoundError as Fobj:
        print("File is not present in current directory")

if __name__ == "__main__":
    main()