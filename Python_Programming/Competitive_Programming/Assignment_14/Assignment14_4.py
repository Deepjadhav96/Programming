
minimum  = lambda X, Y: min(X,Y)

def main():
    iNo1 = int(input("Enter a number : "))
    iNo2 = int(input("Enter a second number: "))
    
    Ret = minimum(iNo1,iNo2)
    print("Minimum number is: ",Ret)


if __name__ == "__main__":
    main()