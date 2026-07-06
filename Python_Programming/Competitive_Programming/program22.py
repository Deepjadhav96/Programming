
def area(radius):
    return 3.14 * radius * radius

def main():
    rad = int(input("Enter a radius: "))
    

    result = area(rad)
    print("Area of circle:",result)
     
if __name__ == "__main__":
    main()