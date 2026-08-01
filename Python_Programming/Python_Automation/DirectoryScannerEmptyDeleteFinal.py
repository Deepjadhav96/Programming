###############################################################
#
#  Importing required libraries
#
################################################################

import sys
import os
import time 
import schedule
###############################################################
#
#   Function Name:  DirectoryScanner
#   Input :         Name of Directory
#   Descrption:     Deletes all empty file periodically
#   Date :          19/07/2026
#   Author :        Deep Manohar Jadhav
#
################################################################
def DirectoryScanner(DirectoryPath="Marvellous"):
    Border = "_"*40

    timestamp = time.ctime()
    
    LogFileName = "Marvellous%s.log"%(timestamp)
    LogFileName = LogFileName.replace(" ","_")
    LogFileName = LogFileName.replace(":","_")

    Ret = False
    Ret = os.path.exists(DirectoryPath)

    if(Ret == False):
        print("Marvellous Automation Error : There is no such directory with name",DirectoryPath)
        return
    
    Ret = os.path.isdir(DirectoryPath)
    if Ret == False:
        print("Marvellous Automation Error : It is not a directory with name ",DirectoryPath)
        return

    print("Log file name gets created with name :",LogFileName)

    fobj = open(LogFileName,"w")

    fobj.write(Border+"\n")

    fobj.write("Marvellous Automation Scrpit\n")

    fobj.write(Border+"\n\n")

    fobj.write("Files from directory are :\n\n")
    fobj.write(Border+"\n")

    TotalFiles = 0
    EmptyFiles = 0

    for FolderName, SubFolder, FileName in os.walk(DirectoryPath):
        for fname in FileName:
            TotalFiles = TotalFiles + 1
            fname = os.path.join(FolderName, fname)
            fobj.write(f"{fname}:{os.path.getsize(fname)} bytes\n")

            if(os.path.getsize(fname) == 0): 
                 EmptyFiles = EmptyFiles + 1
                 os.remove(fname)   

    fobj.write(Border+"\n")

    fobj.write(f"Total file scanned :{TotalFiles}\n")
    fobj.write(f"Total empty files found and deleted :{EmptyFiles}\n")

    fobj.write(Border+"\n")

    fobj.write("LogFile gets created at :"+timestamp)
    fobj.write("\n"+Border+"\n")

    fobj.close()
###############################################################
#
#   Function Name:  main
#   Input :         Command line arguments
#   Descrption:     It controls the script
#   Date :          19/07/2026
#   Author :        Deep Manohar Jadhav
#
################################################################
def main():

    Border = "-"*80
    print(Border)
    print("Marvellous Automation Scrpit")
    print(Border)

    if ((len(sys.argv)) == 2 ):

        if(sys.argv[1]=="--h" or sys.argv[1]=="--H"):
            print("This automation scrpit is used to travel the directory")
            print("For better usage please check --u flag")
        elif(sys.argv[1]=="--u" or sys.argv[1]=="--U"):
            print("Please execute the scrpit as ")
            print("Python FileName.py DirectoryName")
            print("DirectoryName should be absolute path")
        else:
        #    DirectoryScanner(sys.argv[1])
          schedule.every(1).minute.do(DirectoryScanner, sys.argv[1])

        while True:
               schedule.run_pending()
               time.sleep(1)
           
    print(Border)
    print("Thank you for using Marvellous Automation Scrpit")
    print(Border)

###############################################################
#
#   Starter of the automation script
#
################################################################
if __name__ == "__main__":
    main()

#files not get Deleted