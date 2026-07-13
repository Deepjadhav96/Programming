def ChkSum(No):
    if(No % 2 == 0):
        print(f"{No} is even")
    else:
        print(f"{No} is odd")
        
def main():
    print("Enter a number: ")
    Value = int(input())
    ChkSum(Value)
if __name__ == "__main__":
    main()
