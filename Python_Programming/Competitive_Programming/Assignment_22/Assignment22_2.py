import time
import multiprocessing
import os

def FactorialsNo(No):
    print("Process is running with PID :",os.getpid())
    fact = 1
    for i in range(No+1,1,-1):
        fact = i * fact
    print(fact)

def main():
    Data = [10000000, 20000000, 30000000, 40000000, 50000000]
    Result = []

    start_time = time.perf_counter()

    pobj = multiprocessing.Pool() 

    Result = pobj.map(FactorialsNo , Data)  # map() from pool class

    pobj.close()
    pobj.join()

    end_time = time.perf_counter()

    print("Result is: ")
    print(Result)

    print(f"Time required : {end_time-start_time:.4f} seconds")

if __name__ == "__main__":
    main()
