from transformers import AutoTokenizer

#Load pre-trained tokenizer

tokenizer = AutoTokenizer.from_pretrained("gpt2")

# Input Sentence
sentence = "Python is easy programming language I love it"

# Convert the sentence into tokens
tokens = tokenizer.tokenize(sentence)

token_ids = tokenizer.encode(
    sentence,
    add_special_tokens = False
)

#Convert token id back to text
decoded = tokenizer.decode(token_ids)

print("Original sentensce: ",sentence)

print("Token: ",tokens)
print("Token id: ",token_ids)

print("Decoded sentence: ",decoded)