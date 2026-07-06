def DisplaySquare(A):
    return A * A

def main():
    A = int(input("Enter a number:"))
    Sqr = DisplaySquare(A)

    print("Sqaure is ",Sqr)
    
if __name__=="__main__":
     main()