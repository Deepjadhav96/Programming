import schedule
import time 
import datetime

def Display():
    print("Jay ganesh....",datetime.datetime.now())

def main():
    print("Automation script started")

    schedule.every(10).seconds.do(Display)    
    while(True):
        schedule.run_pending()
        time.sleep(1)

    print("End of Automation scrpit")
if __name__=="__main__":
    main()