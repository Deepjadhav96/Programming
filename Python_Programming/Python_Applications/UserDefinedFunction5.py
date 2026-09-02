#Accept: Multiple Parameters
#Return: Multiples Values

def Marvellous(Value1, Value2):
    print("Inside Marvellous : ",Value1,Value2)
    return 21,51

def main():
    Ret1 , Ret2 = Marvellous(10,20)
    print("Return value is : ",Ret1,Ret2)

if __name__ =="__main__":
    main()