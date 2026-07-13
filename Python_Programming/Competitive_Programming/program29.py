from functools import reduce
Addition = lambda No1, No2: No1 + No2

def main():
    Values = [11,22,124,145,87,654,231]
    
    FData = reduce(Addition, Values)
    
    print("Addition of numbers in list are :",FData)
    
if __name__ == "__main__":
    main()
