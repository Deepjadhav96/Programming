def Addition(No1, No2):
    return No1 + No2
        
def main():
    print("Enter a first number: ")
    Value1 = int(input())
    
    print("Enter second number: ")
    Value2 = int(input())

    Ret = Addition(Value1, Value2)
    print("Addition is : ",Ret)
    
if __name__ == "__main__":
    main()
