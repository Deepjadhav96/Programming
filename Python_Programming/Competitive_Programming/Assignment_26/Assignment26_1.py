class Demo:
    value1 = 10
    def __init__(self,A,B):
        self.No1 = A
        self.No2 = B

    def Fun(self):
        print(self.No1) 
        print(self.No2) 

    def gun(self):
        print(self.No1) 
        print(self.No2)



dobj1 = Demo(51,21)
dobj2 = Demo(11,21)

dobj1.Fun()
dobj2.Fun()

dobj1.gun()
dobj2.gun()
