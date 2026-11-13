import schedule
import datetime
import time
def codingkar():
      print("Coding kar...")
def main():
        schedule.every(30).minute.do(codingkar)

        while True:
               schedule.run_pending()
               time.sleep(1)
           

if __name__ == "__main__":
    main()
