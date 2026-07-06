
def primeNo(No):
    count = 0
    for i in range(2,No):
        if(No % i == 0):
            count = count +1
    return count



def main():
    value = int(input("Enter a number : "))
    Result = primeNo(value)
    if (Result >= 1 ):
        print("Number is not prime")
    else:
        print("Number is prime")

if __name__=="__main__":
    main()