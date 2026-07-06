def Factorial(No):
    fact = 1
    for i in range(No,1,-1):
        fact = fact * i
    return fact
    
def main():
    value = int(input("Enter a number: "))
    Result = Factorial(value)
    print("Factorail of no is: ",Result)


if __name__ == "__main__":
    main()