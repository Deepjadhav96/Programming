def factorial(No):
    Fact = 1
    for i in range(1,No+1):
        Fact = Fact * i
    return Fact

def main():
    Value = int(input("Enter number:"))

    Ret = factorial(Value)

    print(f"Factorial of {Value} is {Ret}") #f is from printf
if __name__ == "__main__":
    main()