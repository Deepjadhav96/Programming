import schedule
import datetime
import time
def LunchTime():
      print("Lunch Time...")
def Wrapup():
      print("Wrap up .....")

def main():
        schedule.every().day.at("12:57").do(LunchTime)
        schedule.every().day.at("18:00").do(Wrapup)
        
        while True:
               schedule.run_pending()
               time.sleep(1)
  

if __name__ == "__main__":
    main()
