
cube  = lambda X: X * X *X

def main():
    iNo = int(input("Enter a number : "))
    Ret = cube(iNo)
    print("Cube of number: ",Ret)


if __name__ == "__main__":
    main()