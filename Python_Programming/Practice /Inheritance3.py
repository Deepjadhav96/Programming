class Base:
    def __init__(self):
        print("Inside Base constructor")

class Derived(Base):
    def __init__(self):
        super().__init__()              #explicitly called init of Base class
        print("Inside Derived constructor")

dobj = Derived()            #self vs super


