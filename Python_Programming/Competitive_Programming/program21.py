
def area(len, wid):
    return len * wid

def main():
    length = int(input("Enter a length: "))
    width = int(input("Enter a width :"))

    result = area(length, width)
    print("Area of rectangle:",result)
     
if __name__ == "__main__":
    main()