def CheckVowel(ch):
    if ch == 'a' or ch =='e' or ch =='i' or ch =='o' or ch=='u':
        print("Its vowel")
    else:
        print("Its not vowel")
        
def main():
    value = (input("Enter a character : "))
    CheckVowel(value)
    
if __name__=="__main__":
    main()