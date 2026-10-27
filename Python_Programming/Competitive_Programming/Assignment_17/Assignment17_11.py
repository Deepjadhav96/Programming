# 9. Count Digits

# Write a program which accepts a number from the user and returns the number of digits in that number.

# Input: 5187934

# Output: 7


def countDigits(No):
    counti = 0
    while No != 0:
        iDigit = No % 10
        counti = counti + 1
        No = No // 10

    return counti

def main():
    iNo = int(input("Enter a number:"))
    result = countDigits(iNo)
    print("Digit count:",result)
if __name__ == "__main__":
    main()