import schedule
import time
def printer1():
      print("Jay Ganesh...")
def main():
        schedule.every(1).minute.do(printer1)

        while True:
               schedule.run_pending()
               time.sleep(1)
           

if __name__ == "__main__":
    main()
