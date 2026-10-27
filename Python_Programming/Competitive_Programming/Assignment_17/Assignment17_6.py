# Addition of Factors

# Write a program which accepts one number from the user and returns the addition of its factors.

# Input: 12

# Output: 16 (1 + 2 + 3 + 4 + 6)

def AddFactorial(No):
    Addfact = 0
    start = int(No / 2)
    for i in range(start,0,-1):
        if (No % i == 0):
            Addfact = Addfact + i

    return Addfact
           
def main():
    Value = int(input("Enter your number: "))
    Ret = AddFactorial(Value)


    print("Factorial is :",Ret)
    
if __name__ == "__main__":
    main()