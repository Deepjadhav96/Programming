# Factorial

# Write a program which accepts one number from the user and returns its factorial.

# Input: 5

# Output: 120
def Factorial(No):
    fact = 1
    for i in range(No+1,0,-1):
        fact = fact * i
    return fact
           
def main():
    Value = int(input("Enter your number: "))
    Ret = Factorial(Value)


    print("Factorial is :",Ret)
    
if __name__ == "__main__":
    main()
