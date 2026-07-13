from functools import reduce
Minimum = lambda a , b: a if a < b else b 

def main():
    Values = [11,22,124,145,87,654,231]
    
    FData = reduce(Minimum, Values)
    
    print("Maximum numbers in list are :",FData)
    
if __name__ == "__main__":
    main()
