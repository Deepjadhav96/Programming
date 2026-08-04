import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split

from sklearn.tree import DecisionTreeClassifier

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

############################################################
##     Step 5 : Split the Dataset for training and testing
############################################################

print(Border)
print("Step 5 :Split the Dataset for training and testing")
print(Border)

X_train ,X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.5,random_state=42)
print("Dataset splitting activity done")

print("X : ",X.shape)       #(150,4)
print("Y : ",Y.shape)       #(150,)

print("X_train: ",X_train.shape)        #(75,4)
print("X_test: ",X_test.shape)          #(75,4)

print("Y_train: ",Y_train.shape)    #(75,)
print("X_train: ",Y_test.shape)     #(75,)


############################################################
##     Step 6 : Build the model
############################################################

print(Border)
print("Step 6 : Build the model")
print(Border)


model = DecisionTreeClassifier(max_depth=5)

print("Model gets created succesfully....")


############################################################
##     Step 7 : Train the model
############################################################

print(Border)
print("Step  : Train the model")
print(Border)

model.fit(X_train, Y_train)

print("Model trained successfully...")

############################################################
##     Step 8 : Test the model
############################################################

print(Border)
print("Step 8 : Test the model")
print(Border)

Y_pred = model.predict(X_test)

print("Model testing done")

print("Expected answer :")
print(Y_test)

print("Predicted answer :")
print(Y_pred)