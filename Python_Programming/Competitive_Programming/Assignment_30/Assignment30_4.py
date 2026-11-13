import schedule
import datetime
import time
def Namskar():
      print("Namskar...")
def main():
        schedule.every().day.at("09:00").do(Namskar)

        while True:
               schedule.run_pending()
               time.sleep(1)
           

if __name__ == "__main__":
    main()
