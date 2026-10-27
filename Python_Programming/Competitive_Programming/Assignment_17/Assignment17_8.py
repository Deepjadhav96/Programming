# Display the Following Pattern

# Input: 5

# *   *   *   *  *
# *   *   *   *
# *   *   *
# *   *
# *

def pattern(No):
    for i in range(No):
        for j in range(No-i):
            print("*", end=" ")
        
        print()
def main():
    Value = int(input("Enter your number: "))
    pattern(Value)
    
if __name__ == "__main__":
    main()
