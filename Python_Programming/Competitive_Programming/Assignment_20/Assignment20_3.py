import threading
import time

def EvenAdd(*args1):
    sum = 0
    for i in args1:
        if i % 2 == 0:
                 sum = sum + i
    print(sum)
             
def OddAdd(*args2):
    sum = 0
    for i in args2:
        if i % 2 == 1:
                 sum = sum + i
    print(sum)
      
def main():
    t1 = threading.Thread(target = EvenAdd, args = [2,3,4,3,6])
    t2 = threading.Thread(target = OddAdd, args = [3,9,12,4,1])
    
    t1.start()
    t1.join()
    
    t2.start()
    t2.join()
    
    print("Exit from main()")
if __name__ =="__main__":
    main()
