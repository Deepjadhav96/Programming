Square = lambda No: No * No



def main():
    Values = [11, 21, 51, 101]
    Ret = list(map(Square, Values))
    
    print("Square of values are:",Ret)
    
if __name__ == "__main__":
    main()
