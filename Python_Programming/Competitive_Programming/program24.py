def Binary(No):
    
    Bin = (bin(No))
    return Bin
    

def main():
    value = int(input("Enter a number:"))
    Bin = Binary(value)

    print("Binary is ",Bin)
    
if __name__=="__main__":
     main()