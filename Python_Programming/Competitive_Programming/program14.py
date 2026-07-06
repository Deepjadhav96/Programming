
def reversedNumber(No):
    reversed = []
    while (No != 0):
        Digit = int(No % 10)
        reversed.append(Digit)
        No = int(No / 10)
    return reversed  

def main():
    value = int(input("Enter a number : "))
    Result =  reversedNumber(value)
    print("Reversed number :",Result)
if __name__=="__main__":
    main()