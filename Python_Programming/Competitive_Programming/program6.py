def table(No):
    
    for i in range(1,11):
        table = No * i
        print(table)



def main():
    value = int(input("Enter a number: "));
    table(value)


if __name__ == "__main__":
    main()