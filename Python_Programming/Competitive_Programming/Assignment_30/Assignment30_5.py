import schedule
import datetime
import time
def ScheduleTask(fobj):
      timestamp = time.strftime("%d-%m-%Y %H-%M-%S")
      fobj.write(f"Current Date and time: {timestamp}\n")
def main():
      fobj = open("Marvellous.txt","a")

      schedule.every(3).seconds.do(ScheduleTask,fobj)

      while True:
               schedule.run_pending()
               time.sleep(1)
           

if __name__ == "__main__":
    main()
