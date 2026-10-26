
maximum = lambda X,Y,Z: X if (X>Y or X>Z)  else ( Y if Y>Z else Z)

def main():
    iNo1 = int(input("Enter a first number : "))
    iNo2 = int(input("Enter a second number : "))
    iNo3 = int(input("Enter a third number : "))
    
    Ret = maximum(iNo1,iNo2,iNo3)
    print("Max number is: ",Ret)

if __name__ == "__main__":
    main()