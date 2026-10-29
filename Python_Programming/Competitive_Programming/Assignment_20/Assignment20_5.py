import threading
import time

def thread1(No):
    for i in range(1,No+1):
        print(i)
    print("First thread completed")

def thread2(No):
    for i in range(50,No,-1):
        print(i)
    print("Second thread completed")

def main():
    t1 = threading.Thread(target = thread1, args = (50,))
    t2 = threading.Thread(target = thread2, args =(0,))
    
    t1.start()
    t1.join()
    
    t2.start()
    t2.join()
      
   
    
if __name__ =="__main__":
    main()
