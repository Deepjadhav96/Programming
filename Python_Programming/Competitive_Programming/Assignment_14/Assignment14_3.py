
maximum  = lambda X, Y: max(X,Y)

def main():
    iNo1 = int(input("Enter a number : "))
    iNo2 = int(input("Enter a second number: "))
    
    Ret = maximum(iNo1,iNo2)
    print("Maximum number is: ",Ret)


if __name__ == "__main__":
    main()