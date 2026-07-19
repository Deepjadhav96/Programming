class Arithmetic:
    def Addition(No1, No2):
        Ans = No1 + No2
        return Ans

    def Substraction(No1, No2):
        Ans = No1 - No2
        return Ans
    
Aobj = Arithmetic()

print("Enter first number:")
Value1 = int(input())

print("Enter second number:")
Value2 = int(input())

#Ret = Addition(Aobj, Value1, Value2)
Ret = Aobj.Addition(Value1 , Value2)            #Issue
print("Addition is :",Ret)

Ret = Aobj.Substraction(Value1, Value2)
print("Substraction is :",Ret)

