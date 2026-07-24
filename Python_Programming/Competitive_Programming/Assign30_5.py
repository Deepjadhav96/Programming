import schedule

import time 

def task1():
    timestamp = time.ctime()
    try:
        fopen = open("Marvellous.txt",'a')

     
        fopen.write(f"Task executed at :{timestamp}\n")
        print("Written inside the log file")
      
    except FileNotFoundError as fobj:
        print("File is not found in this current directory")

    fopen.close()

def main():
    
    schedule.every(5).minutes.do(task1)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__=="__main__":
    main()

    