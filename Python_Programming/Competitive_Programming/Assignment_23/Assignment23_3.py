import time
import multiprocessing
import os

def Evencount(No):
    print("Process is running with PID :",os.getpid())
    print("Input number is: ",No)
    EvenCount = 0
    for i in range(1,No+1):
        if i % 2 == 0:
            EvenCount = EvenCount + 1
    return EvenCount

def main():
    Data = [5, 20, 300, 40, 500]
    Result = []

    start_time = time.perf_counter()

    pobj = multiprocessing.Pool() 

    Result = pobj.map(Evencount , Data)  # map() from pool class

    pobj.close()
    pobj.join()

    end_time = time.perf_counter()

    print("Count of Even numbers: ")
    print("Count of Even numbers: ")
    print(Result)

    print(f"Time required : {end_time-start_time:.4f} seconds")

if __name__ == "__main__":
    main()
