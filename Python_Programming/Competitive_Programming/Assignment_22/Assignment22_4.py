import time
import multiprocessing
import os

def FactorialsNo(No):
    print("Process is running with PID :",os.getpid())
    Sum = 0
    for i in range(No+1):
        Sum = Sum + (i ** 5)
    return Sum

def main():
    Data = [5, 20, 300, 40, 500]
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
