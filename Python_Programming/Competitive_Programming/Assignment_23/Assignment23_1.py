import time
import multiprocessing
import os

def Evensum(No):
    print("Process is running with PID :",os.getpid())
    print("Input number is: ",No)
    EvenSum = 0
    for i in range(No+1):
        if i % 2 == 0:
            EvenSum = EvenSum + i
    return EvenSum

def main():
    Data = [5, 20, 300, 40, 500]
    Result = []

    start_time = time.perf_counter()

    pobj = multiprocessing.Pool() 

    Result = pobj.map(Evensum , Data)  # map() from pool class

    pobj.close()
    pobj.join()

    end_time = time.perf_counter()

    print("Sum of even numer is: ")
    print(Result)

    print(f"Time required : {end_time-start_time:.4f} seconds")

if __name__ == "__main__":
    main()
