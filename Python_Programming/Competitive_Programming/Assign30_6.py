import schedule
import time 
import datetime

def task1():
    print("Lunch time \n")

def task2():
    print("Wrapup time \n")


def main():
    schedule.every().day.at("13:00").do(task1)
    schedule.every().day.at("16:00").do(task1)

    while True:
        schedule.run_pending
        time.sleep(1)

if __name__ == "__main__":
    main()