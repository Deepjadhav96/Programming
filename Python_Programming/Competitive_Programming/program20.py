def manyNumber(No):
    for i in range(No,0,-1):
        print(i)

def main():
    value = int(input("Enter a number: "))
    manyNumber(value)    


if __name__ == "__main__":
    main()