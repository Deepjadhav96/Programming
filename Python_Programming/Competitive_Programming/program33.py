Divisible = lambda No: No if (No%3==0) and (No%5==0) else None


def main():
    Values = [15,45,195,39,22]
    
    Ret = list(filter(Divisible , Values))
    
    print("Numbers in list which are divisible by 3 and 5 :",Ret)
    

    
if __name__ == "__main__":
    main()
