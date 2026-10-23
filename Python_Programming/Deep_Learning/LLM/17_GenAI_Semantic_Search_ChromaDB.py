from sentence_transformers import SentenceTransformer,util
import chromadb

#Load pretrained embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

#Knowledge Base
documents = [
    "Python is used for machince learning",
    "Java is used for enterprise application",
    "SQL is used to manage  databases",
    "HTML is used to create web pages",
    "Tensorflow is used for deep learning"

]

#genrate document embedding
document_embedding = model.encode(documents,convert_to_tensor = True)


#Create chromadb client 
client = chromadb.PersistentClient(path = "./MarvellousDB")

#Create collection
collection = client.get_or_create_collection(
    name = "marvellous_knowledge",
    configuration={"hsnw":{"space":"cosine"}}
)#hsnwm --> Hierarchical Navigable Small world

#Store documents and embeddings

collection.upsert(
    ids = ["doc1","doc2","doc3","doc4","doc5"],
    documents = documents,
    embeddings = document_embedding.tolist()
)

print("Total documents : ",collection.count())

#Accept question
query = input("Enter your question :")

#genrate document embedding
query_embedding = model.encode(query,convert_to_tensor = True)

scores = util.cos_sim(query_embedding,document_embedding)[0]

#Find top 2 matching documents
top_result = scores.topk(2)

print("Top 2 relevant document :")

for index in top_result.indices:
    print(documents[index.item()])
    



