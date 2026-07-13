LengthChecker = lambda names: names if len(names) > 5 else None


def main():
    Values = ["Dp","Manohar","Jadhav"]
    
    Ret = list(filter(LengthChecker , Values))
    
    print("String length > 5 are :",Ret)
    

    
if __name__ == "__main__":
    main()
