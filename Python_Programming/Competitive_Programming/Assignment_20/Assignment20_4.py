import threading
import time

def Small(*args):
    count = 0
    for char in args:
        if char .islower():
            print(char,end=" ")
            count += 1
    print("Count of small letters: ",count)
    print("Thread ID: ",threading.get_ident())
def Capital(*args):
    count = 0
    for char in args:
        if char .isupper():
            print(char,end=" ")
            count += 1
    print("Count of capital letters: ",count) 
    print("Thread ID: ",threading.get_ident())
def Digit(*No):
   count = 0
   for char in No:
        if char .isdigit():
            print(char,end=" ")
            count += 1
   print("Count of digits are: ",count)
   print("Thread ID: ",threading.get_ident())
    
def main():
    t1 = threading.Thread(target = Small, args = "Deep")
    t2 = threading.Thread(target = Capital, args ="DEEP")
    t3 = threading.Thread(target = Digit, args ="10Deep")
    
    t1.start()
    t1.join()
    
    t2.start()
    t2.join()
      
    t3.start()
    t3.join()
    
if __name__ =="__main__":
    main()
