import threading 

def Prime(*args1):
    print("Non prime numbers are: ")
    for num in args1:
        count = 0
        
        for i in range(1,num+1):
            if  num % i == 0:
                count += 1
        if count == 2:
            print(num)
def NonPrime(*args1):
    print("Non prime numbers are: ")
    for num in args1:
        count = 0
        
        for i in range(1,num+1):
            if  num % i == 0:
                count += 1
        if count > 2:
            print(num)
def main():
    Data = [11,21,51,101,512,241,43,47,51,53,68]
    t1 = threading.Thread(target = Prime,args = (*Data,))  
    t2 = threading.Thread(target = NonPrime,args = (*Data,))   
    
    t1.start()
    t1.join()
    
    t2.start()
    t2.join()
    
  
if __name__ == "__main__":
    main()
