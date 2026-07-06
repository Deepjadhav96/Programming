def SumOfNo(No):
    Sum = 0
    for i in range(1,No+1):
        Sum = Sum + i
    return Sum

def main():
    value = int(input("Enter a number: "));
    iRet = SumOfNo(value)

    print("Sum of Nth natural number is:",iRet)


if __name__ == "__main__":
    main()