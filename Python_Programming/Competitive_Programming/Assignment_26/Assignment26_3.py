class Arithmetic:
    def __init__(self):
        self.Value1 = 0
        self.value2 = 0

    def Accept(self,No1,No2):
        self.Value1 = No1
        self.Value2 = No2
        
    def Addition(self):
        Add = self.Value1 + self.Value2
        return Add

    def Subtraction(self):
        Subs = self.Value1 - self.Value2
        return Subs

    def Multiplication(self):
        Mult = self.Value1 * self.Value2
        return Mult

    def Division(self):
        Div = self.Value1 / self.Value2
        return Div

def main():
    No1 = float(input("Enter first number: "))
    No2 = float(input("Enter second number: "))

    aobj = Arithmetic()

    aobj.Accept(No1,No2)
    print("Addition is : ",aobj.Addition())

    print("Substraction is: ",aobj.Subtraction())

    print("Multiplicaton is :",aobj.Multiplication())

    print("Division is : ",aobj.Division())
    
if __name__ == "__main__":
    main()