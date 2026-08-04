import pandas as pd

Border ="-"*30

#############################################
##      Step 1 : Load the dataset
#############################################

print(Border)
print("Step 1 : Load the dataset")
print(Border)

Datapath = "iris.csv"

df = pd.read_csv(Datapath)      #df ->Dataframe     

print("Dataset loaded successfully..")

print("Initial entries from Dataset are: ")
print(df.head())