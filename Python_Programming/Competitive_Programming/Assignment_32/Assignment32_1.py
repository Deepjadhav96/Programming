import schedule
import time 
import os

def texFileGenerator():
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    FileName = os.path.join(f"File_%s.log"%timestamp)

    fobj = open(FileName,"w")

    print("File gets created successfully")

def main():
    print("Automation script started")
    schedule.every(10).minutes.do(texFileGenerator)

    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()