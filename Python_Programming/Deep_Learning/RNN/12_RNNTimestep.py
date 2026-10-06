sentence = "food was not good"
#Timestep      1   2   3    4
#Token         1   2   5    3
words = sentence.split()

print("Actual sentence: ",sentence)

for index,word in enumerate(words):
    print("Timestep: ",index+1," : ",word)
