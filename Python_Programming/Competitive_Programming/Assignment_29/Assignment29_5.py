import sys

def FrequencyOfWord(FileName1,word):
    counter = 0
    Data = FileName1.read()
    tokens = Data.split()

    for Token in tokens:
        if word.lower() == Token.lower():
             counter = counter + 1

    return counter
def main():
    try:
        FileName1 = open(sys.argv[1],"r")
        word = sys.argv[2]
        
        Result = FrequencyOfWord(FileName1,word)
        
    except FileNotFoundError as fobj:
        print("File is not present in the current directory")

    
    print(f"Frequency of {word} is :",Result)
if __name__=="__main__":
    main()

