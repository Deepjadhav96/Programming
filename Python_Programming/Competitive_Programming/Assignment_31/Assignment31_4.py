import schedule
import time
import os



def LogFileGenerator(LogName):
    print("Log filegenerator script started...")

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    FileName = os.path.join(f"{LogName}_%s.log"%timestamp)

    fobj = open(FileName,"w")

    print(f"Log file gets successfully created with name {FileName}")
def main():
    
    LName = input("Enter a  Log file name : ")

    schedule.every(5).seconds.do(LogFileGenerator,LName)
    print("Automation script started:")
    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()