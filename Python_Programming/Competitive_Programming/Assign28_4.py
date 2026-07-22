import shutil
def main():
    try:
        
        shutil.copyfile("Description.txt","Demo.txt")

        print("File content is copied...")

    except FileNotFoundError as fobj:
        print("File is not found in the directory")
if __name__ == "__main__":
    main()