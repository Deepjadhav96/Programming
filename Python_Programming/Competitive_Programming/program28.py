CheckOdd = lambda No: (No % 2 == 1)

def main():
    Values = [11,22,124,145,87,654,231]
    
    FData = list(filter(CheckOdd, Values))
    
    print("Even numbers in list are :",FData)
    
if __name__ == "__main__":
    main()
