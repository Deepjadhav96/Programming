import threading 

def SumOfAll(*args1):
    Sum = 0
    for num in args1:
        Sum = Sum + num
        
    print("Sum is: ",Sum)

def ProdOfAll(*args1):
    product = 1
    for num in args1:
        product = product * num
    print("Product is :",product)
       
def main():
    Data = [11,21,51,101,512,241,43,47,51,53,68]
    t1 = threading.Thread(target = SumOfAll,args = (*Data,))  
    t2 = threading.Thread(target = ProdOfAll,args = (*Data,))   
    
    t1.start()
    t1.join()
    
    t2.start()
    t2.join()
    
  
if __name__ == "__main__":
    main()
