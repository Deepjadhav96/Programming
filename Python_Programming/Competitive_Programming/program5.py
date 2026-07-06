def divisible(A):
    if A % 3 == 0 and A % 5 ==0:
        return True

def main():
    A = int(input("Enter a number:"))
    Sqr = divisible(A)

    if Sqr == True :
        print("Number is Divisible by 3 and 5")
    else :
        print("Number is not Divisible by 3 and 5")       
if __name__=="__main__":
     main()