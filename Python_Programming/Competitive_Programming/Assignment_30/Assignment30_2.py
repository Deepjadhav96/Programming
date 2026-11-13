import schedule
import datetime
import time
def Timer1():
      #strftime==> convert into string
      timestamp = time.strftime("%d-%m-%Y %H-%M-%S")
      print(f"Current Date and time: {timestamp}")
def main():
        schedule.every(1).minute.do(Timer1)

        while True:
               schedule.run_pending()
               time.sleep(1)
           

if __name__ == "__main__":
    main()
