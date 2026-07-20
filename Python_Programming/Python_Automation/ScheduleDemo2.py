import schedule
import time 
import datetime

def Display():
    print("Jay ganesh....",datetime.datetime.now())
def main():
    print("Automation script started")

    schedule.every(1).minute.do(Display)    
    #issue in above line
if __name__=="__main__":
    main()