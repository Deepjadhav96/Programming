import sys
def main():
    try:
        fopen = open(sys.argv[1],'r')
        Data = fopen.read()
        Data1 = Data.split()
        count = 0
        for ch in Data1:
            if ch == sys.argv[2]:
                count = count + 1
        print(f"Count of {sys.argv[2]} in file {sys.argv[1]} is :{count}")

    except FileNotFoundError as fobj:
        print("file is not present in current directory")

if __name__ == "__main__":
    main()