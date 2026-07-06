def addition(No1, No2):
    return No1 + No2

def subtraction(No1, No2):
    return No1 - No2

def multiplication(No1, No2):
    return No1 * No2

def division(No1, No2):
    return No1 / No2

def main():
    value = int(input("Enter a number: "))
    
    result = addition(value)
    print("Addition is :",result)

    result = subtraction(value)
    print("Subtraction is :",result)

    result = multiplication(value)
    print("Multiplication is :",result)

    result = division(value)
    print("Division is :",result)
    

if __name__ == "__main__":
    main()