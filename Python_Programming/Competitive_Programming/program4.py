def DisplayCube(A):
    return A * A * A

def main():
    A = int(input("Enter a number:"))
    Sqr = DisplayCube(A)

    print("Cube is ",Sqr)
    
if __name__=="__main__":
     main()