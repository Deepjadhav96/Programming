
#Step 1: Import required lib

from tensorflow.keras.datasets import imdb
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding,LSTM, Dense
from tensorflow.keras.preprocessing.sequence import pad_sequences

#########################################
#Step 2: Configuration of values
#########################################

VOCAB_SIZE = 10000  #Consider most frequent 10000 unique word
MAX_LENGTH = 200    #Consider maximum 200 words in review


#########################################
# Step3: Load the IMDB(Internet Movie Database) Dataset
#########################################
print("-"*40)
print("Movie review sentiment analysis using LSTM")
print("-"*40)

print("Loading the Dataset")

(X_train, Y_train) , (X_test, Y_test) = imdb.load_data(num_words = VOCAB_SIZE)

print("IMDB Dataset loaded successfully")

print("Number of Training reviews : ",len(X_train))
print("Number of Testing reviews : ",len(X_test))

#########################################
#
#   X_train  Reviews used for training
#   Y_train  Actual sentiments of training
#   X_test   Reviews used for testing
#   Y_test   Actual sentiments of testing
#
#   Sentiments: 
#   0 -> Negative sentiment
#   1 -> Positive sentiment
#########################################

#########################################
#Step4: Load the word dictionary
#########################################

word_index = imdb.get_word_index()

#Exapmle:
#Dictionary contains mapping of words and its corresponding number
# drishyam is good movie (20 56 78 43)
# 20 -> drishyam
# 56 -> is
# 78 -> good
# 43 -> movie

#########################################
# Step5: Create a reverse dictionary
#########################################

reverse_word_index = {}

for word,index in word_index.items():
    reverse_word_index[index + 3] = word


#########################################
#
#########################################