
def printDigit(No):
    
    while (No != 0):
        Digit = int(No % 10)
        print(Digit)
        No = int(No / 10)
        

def main():
    value = int(input("Enter a number : "))
    printDigit(value)
   
if __name__=="__main__":
    main()