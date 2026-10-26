
mult = lambda X,Y: X*Y

def main():
    iNo1 = int(input("Enter a first number : "))
    iNo2 = int(input("Enter a second number : "))
    
    Ret = mult(iNo1,iNo2)
    print("Multiplication is: ",Ret)

if __name__ == "__main__":
    main()