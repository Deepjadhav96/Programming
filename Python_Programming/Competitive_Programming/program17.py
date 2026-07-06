def Factorial(No):
    for i in range(1,No):
        if(No % i == 0):
            print(i)

def main():
    value = int(input("Enter a number: "))
    Factorial(value)
    


if __name__ == "__main__":
    main()