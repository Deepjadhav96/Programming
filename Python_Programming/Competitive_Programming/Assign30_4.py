import schedule
import time 
import datetime

def Display():
   print("Namaskar....")

def main():
    schedule.every().day.at("00:15").do(Display)

    while (True):
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()