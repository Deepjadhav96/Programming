import pandas as pd

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

print("Missing values per columns: ",df.isnull().sum())# Canonical function call

print("Class Distribution (Species count): ")
print(df["species"].value_counts())

print("Statical report of dataset: ")
print(df.describe())

#if missing values occurs -> 1)remove rows
#2) replace missing value with average value of col
#isNull