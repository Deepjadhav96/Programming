sentence = "food was not good"

#Tokenization
words = sentence.split()    

for index,word in enumerate(words):
    print("Position ",index+1,":",word)