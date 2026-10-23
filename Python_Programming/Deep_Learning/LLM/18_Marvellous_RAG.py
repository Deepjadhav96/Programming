from sentence_transformers import SentenceTransformer,util
import chromadb
from ollama import chat

#Load pretrained embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

#Connect to exist chromadb
client  = chromadb.PersistentClient(path = "./MarvellousDB")    

collection = client.get_collection(name="marvellous_knowledge")

#Accept question
query = input("Enter your question :")

#genrate document embedding
query_embedding = model.encode(query,convert_to_tensor = True)

#retrieve top 2 results
results = collection.query(query_embeddings = [query_embedding.tolist()], n_results = 2)

#Create context from retrieved documents
documents = results["documents"][0]

context = "\n".join(documents)

print("Retrieved context : ")
print(context)
