CheckEven = lambda No: (No % 2 == 0)

def main():
    Values = [11,22,124,145,87,654,234]
    
    FData = list(filter(CheckEven, Values))
    
    print("Even numbers in list are :",FData)
    
if __name__ == "__main__":
    main()
