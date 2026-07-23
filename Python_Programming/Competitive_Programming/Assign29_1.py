import pathlib

def main():
      if pathlib.Path("Demo.txt").is_file():
        print("File is exist")
      else:
          print("File is not exist")

if __name__ == "__main__":
    main()