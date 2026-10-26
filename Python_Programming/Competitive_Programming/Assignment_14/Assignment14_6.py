
odd  = lambda X: True if (X%2 != 0) else False

def main():
    iNo1 = int(input("Enter a number : "))
    
    Ret = odd(iNo1)
    if Ret == True:
        print("Number is odd")
    else:
        print("Number is even")
if __name__ == "__main__":
    main()