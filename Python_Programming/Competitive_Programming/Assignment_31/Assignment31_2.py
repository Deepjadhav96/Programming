import schedule
import time



def DisplayMessage(msg):
    print(msg)

def main():
    
    message = input("Enter a  message : ")

    schedule.every(5).seconds.do(DisplayMessage,message)
    print("Automation script started:")
    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()