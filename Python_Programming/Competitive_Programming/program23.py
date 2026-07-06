def perfect(No):
    count = 0
    Sum = 0
    for i in range(1,No):
        if(No % i == 0):
            Sum = Sum + i
    if Sum == No:
        return True        
def main():
    value = int(input("Enter a number: "))
    Result = perfect(value)

    if Result==True:
        print("Number is perfect")
    else:
        print("Number is not perfect")

if __name__ == "__main__":
    main()