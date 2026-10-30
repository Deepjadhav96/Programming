import threading 

def MaxNo(*args1):
    
    for num in args1:
        print(max(num))
        
        
            
def MinNo(*args1):
    
    for num in args1:
        print(min(num))
        
       
def main():
    Data = [11,21,51,101,512,241,43,47,51,53,68]
    t1 = threading.Thread(target = MaxNo,args = (Data,))  
    t2 = threading.Thread(target = MinNo,args = (Data,))   
    
    t1.start()
    t1.join()
    
    t2.start()
    t2.join()
    
  
if __name__ == "__main__":
    main()
