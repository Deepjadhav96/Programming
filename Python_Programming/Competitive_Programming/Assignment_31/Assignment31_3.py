import schedule
import time
import os

def DirectoryScanner():
    for FolderName, SubfolderName, FileName in os.walk("Assignment_30"):
        print(FileName)


def main():
    
    
    schedule.every(5).seconds.do(DirectoryScanner)
    print("Automation script started:")
    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()