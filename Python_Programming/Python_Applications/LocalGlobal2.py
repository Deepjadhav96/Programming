no = 11  #Global Variable

def Display():
    a = 21      #Local Variable
    print("From Display: ",no)
    print("Display value of a: ",a) 

def Demo():     
    print("From Demo: ",no)
    print("From Demo value of a ",a)  #Will generate an error
Display()
Demo()