
divby5 = lambda X: True if (X%5 == 0) else False

def main():
    iNo1 = int(input("Enter a number : "))
    
    Ret = divby5(iNo1)
    if Ret == True:
        print("Number is divisible by 5")
    else:
        print("Number is not divisible by 5")
if __name__ == "__main__":
    main()