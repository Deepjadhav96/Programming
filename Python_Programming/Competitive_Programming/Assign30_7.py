import schedule
import time
import sys
import shutil


def task():
     timestamp = time.ctime()
     try:
         
         file1 = open(sys.argv[1],'r')
         file2 = open(sys.argv[2],'a+')

         shutil.copyfile(sys.argv[1],sys.argv[2])
         file2.write(f"\nBackup is completed at time {timestamp} ")
         
         print(f"Backup of {sys.argv[1]} file is completed to file  {sys.argv[2]}")

         file1.close()
         file2.close()

     except FileNotFoundError as fobj:
        print("File not foun in current directory")
       

def main():

    schedule.every(1).hour.do(task)

    while True:
        schedule.run_pending()
        time.sleep(1)
if __name__ == "__main__":
    main()

      
