from functools import reduce
product = lambda No1, No2: No1 * No2

def main():
    Values = [1, 2, 3, 4]
    Ret = reduce(product, Values)
    print("Product of number of list is:",Ret)
        
if __name__ == "__main__":
    main()
