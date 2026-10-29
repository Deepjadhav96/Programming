import threading
import time

def Even(No):
    for i in range(2,(No*2)+1,2):
        print(i,end = " ")
    print()
        
def Odd(No):
    for i in range(1,(No*2)+1,2):
        print(i,end = " ")
    print()

def main():
    t1 = threading.Thread(target = Even, args = (10,))
    t2 = threading.Thread(target = Odd, args = (10,))
    
    t1.start()
    t1.join()
    
    t2.start()
    t2.join()
    
if __name__ =="__main__":
    main()
