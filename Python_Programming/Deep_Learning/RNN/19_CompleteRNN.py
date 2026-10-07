import numpy as np

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding,SimpleRNN,Dense

#Step1: Load the Data
train_sentences = [
    "food was good",
    "food was bad",
    "food was excellent",
    "food was terrible",
    "service was good",
    "service was bad",
    "service was excellent",
    "service was terrible",
    "ambience was good",
    "ambience was bad",
    "ambience was excellent",
    "ambience was terrible"
]

train_labels = [
    1,
    0,
    1,
    0,
    1,
    0,
    1,
    0,
    1,
    0,
    1,
    0
]

#Step2: Tokenization 

tokenizer = Tokenizer(oov_token = "<OOV>")  #Out Of Vocabulary 

tokenizer.fit_on_texts(train_sentences)

#Step3 : Convert training data into sequence

train_sequence = tokenizer.texts_to_sequences(train_sentences)
print("Training sequences :")

for sentence,sequence in zip(train_sentences, train_sequence):
    print(sentence, " -> ",sequence)


#Step4: Apply padding

max_length = 4

X_train = pad_sequences(
    train_sequence,
    maxlen = max_length,
    padding = "pre"
)

Y_train = np.array(train_labels)

print("Padded training data: ")
print(X_train)

print("Training labels: ")
print(Y_train)
