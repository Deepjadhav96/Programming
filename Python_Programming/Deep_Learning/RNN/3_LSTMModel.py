
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


#########################################################
#   Step6: Function to decode the review (Number to word)
#########################################################

def DecodeReview(encoded_review):
    words = []

    for number in encoded_review:
        if number >= 3:  #Ignore first 3
            word = reverse_word_index.get(number,"?")
            words.append(word)
    
    return " ".join(words) #Join the list of word

#########################################################
#   Step7: Display sample reviews 
#########################################################

print("-"*40)
print("---------Sample Reviews--------")
print("-"*40)

for i in range(4):
    review = DecodeReview(X_train[i])

    print("-"*40)

    print("Review number: ",i+1)
    print("Review : ")
    print(review)

    print("-"*40)


    if Y_train[i] == 1:
        print("Sentiment : Positive")
    else:
        print("Sentiment: Negative")

#########################################################
#   Step 8: Padding  
#########################################################

X_train_padded = pad_sequences(
    X_train,
    maxlen = MAX_LENGTH,
    
)

X_test_padded = pad_sequences(
    X_test,
    maxlen = MAX_LENGTH
)

print("Shape of training data: ",X_train_padded.shape)
print("Shape of testing data: ",X_test_padded.shape)

#########################################################
# Step 9: Create LSTM model
#########################################################

model = Sequential()

model.add(
    Embedding(
        input_dim= VOCAB_SIZE,
        output_dim= 32          #Each word is represented in 32 values
    )
)

model.add(
    LSTM(
        units = 64              #Size of LSTM hidden state
    )        
)

model.add(
    Dense(
        units= 1,               #One Output
        activation= "sigmoid"   #USed to produce probability
    )
    
)

#Project Architecture:
#Review -> Embdding -> LSTM -> Dense -> Sigmoid -> Positive/Negtive

#########################################################
#   Step10 : Compile the model
#########################################################

model.compile(
    optimizer = "adam",                # Algorithm to update weigth
    loss = "binary_crossentropy",      # Loss function
    metrics = ["accuracy"]             # Measure classification accuracy
)

print("Model compiled successfully")

#########################################################
#   Step11: Train the model
#########################################################

print("Model training")

model.fit(
    X_train_padded,          #Input training revies
    Y_train,                 #Actual sentiment labels
    epochs = 3,              #Complete dataset gets processes 3 times
    batch_size = 64,         # Process 64 reviews in one batch
    validation_split = 0.2   #Use 20% training for validation
)

print("Model training gets completed")

#########################################################
# Step 12: Evaluate the model
#########################################################

accuracy = model.evaluate(
    X_test_padded,          #Testing reviews
    Y_test,                  #Actual testing labels
    verbose = 0             #Don't display the process bar on the terminal while display output
)

print("Testing accuracy : ",accuracy)

#########################################################
#   Step13: Predict the review
#########################################################
TEST_REVIEW_NUMBER = 0
original_review = X_test[TEST_REVIEW_NUMBER]
decoded_review = DecodeReview(original_review)

print("Review give to the model : ")
print(decoded_review)

#########################################################
#   Step 14: Get the actual sentiment
#########################################################

actual_value = Y_test[TEST_REVIEW_NUMBER]

if actual_value == 1 :
    actual_sentiment = "POSITIVE"
else:
    actual_sentiment = "NEGATIVE"

print("Actual Sentiment : ",actual_sentiment) 

#########################################################
#   Step 15: Predict the sentiment
#########################################################

review_for_prediction = X_test_padded[TEST_REVIEW_NUMBER : TEST_REVIEW_NUMBER + 1]

prediction = model.predict(
    review_for_prediction,
    verbose = 0
)

probability = prediction[0][0]

if probability >= 0.5:
    predicted_sentiment = "POSITIVE"
else:
    predicted_sentiment = "NEGATIVE"

print("Final prediction is :")

print("-"*40)

print("Prediction probability : ",probability)
print("Actual statement : ",actual_sentiment)
print("Predicted sentiment : ",predicted_sentiment)

print("-"*40)
