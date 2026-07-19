class Demo:
    #class Variables
    Value1 = 10
    Value2 = 20

    def __init__(self):         #Constructor
         self.No1 = 11
         self.No2 = 21

    #Instance method
    def fun(self):
         print("Inside Instance method named as fun()")
         print(self.No1)
         print(self.No2)

         print(Demo.Value1)
         print(Demo.Value2)

    @classmethod
    def gun(cls):
         print("Inside Class method named as fun()")
       #  print(Demo.No1)                               #Not allowed 
       #  print(Demo.No2)
         print(Demo.Value1)
         print(Demo.Value2)

#Call without object
Demo.gun()