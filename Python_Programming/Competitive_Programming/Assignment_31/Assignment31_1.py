import schedule
import time



def Display(msg):
    print(msg)

def main():
    
    message = input("Enter a  message : ")
    timeInterval = int(input("Enter a time interval in seconds: "))
    schedule.every(timeInterval).seconds.do(Display,message)
    print("Automation script started:")
    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()