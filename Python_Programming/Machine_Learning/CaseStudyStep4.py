import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

Border ="-"*30

#############################################
##      Step 1 : Load the dataset
#############################################

print(Border)
print("Step 1 : Load the dataset")
print(Border)

Datapath = "iris.csv"

df = pd.read_csv(Datapath)           

print("Dataset loaded successfully..")

print("Initial entries from Dataset are: ")
print(df.head())


#############################################
##      Step 2 : Data Analysis [EDA]
#############################################

print(Border)
print("Step 2 : Data Analysis")
print(Border)

print("Shape of dataset: ",df.shape)

print("Columns names :",list(df.columns))

print("Missing values per columns: ",df.isnull().sum())

print("Class Distribution (Species count): ")
print(df["species"].value_counts())

print("Statical report of dataset: ")
print(df.describe())


############################################################
##     Step 3 : Decides Independent and Dependent variables
############################################################

print(Border)
print("Step 3 :Decides Independent and Dependent variables")
print(Border)

#X : Independent variable / Features
#Y: Dependent variable / Labels

feature_cols = [
    "sepal length (cm)",
    "sepal width (cm)",
    "petal length (cm)",
    "petal width (cm)"
]

X = df[feature_cols]
Y = df["species"]

print("X shape :",X.shape)
print("Y shape :",Y.shape)

############################################################
##     Step 4 : Visualization of Dataset
############################################################

print(Border)
print("Step 4 :Visualization of Dataset")
print(Border)

#Scatterplot
plt.figure(figsize=(7,5))

for sp in df["species"].unique():
    temp = df[df["species"]==sp]
    plt.scatter(temp["petal length (cm)"] ,temp["petal width (cm)"],label = sp)

plt.title("Marvellous Iris case studies")

plt.xlabel("petal length (cm)")
plt.ylabel("petal width (cm)")

plt.legend()
plt.grid()
plt.show()