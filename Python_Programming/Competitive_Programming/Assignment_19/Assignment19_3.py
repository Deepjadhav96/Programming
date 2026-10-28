from functools import reduce

even = lambda X: ( X % 2 == 0)
sqr = lambda Y: (Y * Y)
addition = lambda A,B:(A+B)

def main():
    lst = list()
    size = 0 
    size = int(input("Number of values to enter: "))

    print("Enter numbers:")
    for i in range(size):
        no = int(input())
        lst.append(no)

   
    evenData = list(filter(even,lst))
    print("Even numbers are: ",evenData)

    sqrData = list(map(sqr,evenData))
    print("Square of even Data: ",sqrData)

    addData = reduce(addition,sqrData)
    print("Addition of even Data: ",addData)

    
if __name__ == "__main__":
    main()
