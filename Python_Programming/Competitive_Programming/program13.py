
def CountDigit(No):
    Count = 0
    while (No != 0):
        Digit = int(No % 10)
        Count =Count +1
        No = int(No / 10)
    return Count  

def main():
    value = int(input("Enter a number : "))
    Result =  CountDigit(value)
    print("Count of Digits in number :",Result)
if __name__=="__main__":
    main()