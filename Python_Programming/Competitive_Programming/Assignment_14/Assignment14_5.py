
even  = lambda X: True if (X%2==0) else False

def main():
    iNo1 = int(input("Enter a number : "))
    
    Ret = even(iNo1)
    if Ret == True:
        print("Number is even")
    else:
        print("Number is odd")
if __name__ == "__main__":
    main()