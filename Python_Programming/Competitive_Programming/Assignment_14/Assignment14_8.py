
Addition = lambda X,Y: X+Y

def main():
    iNo1 = int(input("Enter a first number : "))
    iNo2 = int(input("Enter a second number : "))
    
    Ret = Addition(iNo1,iNo2)
    print("Addition is: ",Ret)

if __name__ == "__main__":
    main()