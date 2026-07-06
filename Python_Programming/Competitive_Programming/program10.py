def odd(No):
    for i in range(1,No+1,2):
     print(i)
    
def main():
    value = int(input("Enter a number: "))
    odd(value)
    


if __name__ == "__main__":
    main()