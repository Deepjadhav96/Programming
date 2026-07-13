CountEven = lambda No1: (No1 % 2 == 0)

def main():
    Values = [101, 121, 151, 160, 34, 56, 98]
    Ret = list(filter(CountEven, Values))  
    print("Count of even number :",len(Ret))
    
    
if __name__=="__main__":
    main()
