# Prime Number

# Write a program which accepts one number from the user and checks whether the number is prime or not.

# Input: 5

# Output: It is Prime Number

def prime(No):
    
    start = int(No / 2)
    for i in range(1,start,-1):
        if (No % i == 0):
                return False
                
                
        
        return True

           
def main():
    Value = int(input("Enter your number: "))
    Ret = prime(Value)

    if(Ret == True):
        print(f"{Value} is prime")
    else:
         print(f"{Value} is not prime")
    
if __name__ == "__main__":
    main()