import threading
import time

def EvenFactor(No):
    sum = 0
    for i in range(2,No):
        if i % 2 == 0:
            if No % i == 0:
                 sum = sum + i
    print(sum)
             
def OddFactor(No):
    sum = 0
    for i in range(1,No):
        if i % 2 == 1:
            if No % i == 0:
                 sum = sum + i
    print(sum)
      
def main():
    t1 = threading.Thread(target = EvenFactor, args = (10,))
    t2 = threading.Thread(target = OddFactor, args = (26,))
    
    t1.start()
    t1.join()
    
    t2.start()
    t2.join()
    print("Exit from main()")
if __name__ =="__main__":
    main()
