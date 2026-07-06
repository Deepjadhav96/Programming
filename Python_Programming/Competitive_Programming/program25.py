def Grade(Marks):
    if Marks >= 75:
        print("Distinction")
    elif Marks >= 60 and Marks < 75:
        print("First class")
    elif Marks >= 50 and Marks < 60:
        print("Second class")
    else:
        print("Fail")

def main():
    value = int(input("Enter a marks : "))
    Grade(value)

if __name__=="__main__":
    main()