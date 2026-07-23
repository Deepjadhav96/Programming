import shutil
import sys
def main():
    try:
        fopen = open(sys.argv[1],'r')
        fopen = open(sys.argv[2],'r')
        
        shutil.copyfile(sys.argv[1],sys.argv[2])
        print(f"Content from {sys.argv[1]} is copied to {sys.argv[2]}")

    except FileNotFoundError as fobj:
        print("File is not found in the directory")
if __name__ == "__main__":
    main()