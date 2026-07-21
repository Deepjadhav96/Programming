
def main():
    try:
        fobj =  open("Demo.txt","r")        
        print("File gets opened")

        Data = fobj.read(5)
        print(Data)

        fobj.seek(10, 1)    #fileLOCK operation         DELETED FILE

        Data = fobj.read(5)
        print(Data)
       
    
    except FileNotFoundError as fobj:
        print("File is not present in current directory")
        
if __name__ == "__main__":
    main()


#seek (kuthe , kuthun)
#kuthun: 0/1/2

#0->start
#1->Current
#2->end