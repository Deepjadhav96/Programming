import pandas as pd
import numpy as np
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score ,confusion_matrix

#Step1: Load the Dataset
#--------------------------------------------------------------
#
#   Function Name: LoadData
#   Descritpion:   Load the Data from CSV
#   Input :        MarvellousTitanicData.csv
#   Output:        Dataframe
#   Author:        Deep Jadhav
#   Date:          16/08/2026
#
#--------------------------------------------------------------

def LoadData(filename):
    df = pd.read_csv(filename)

    print("Dataset loaded succussfully")
    print(df.head())

    return df

#Step2: Data preprocessing
#--------------------------------------------------------------
#
#   Function Name: PreprocessData
#   Descritpion:   Perform Data analysis
#   Input :        DataFrame
#   Output:        Update Dataframe
#   Author:        Deep Jadhav
#   Date:          16/08/2026
#
#--------------------------------------------------------------

def PreprocessData(df):
    df = df.drop([
        "Passengerid",
        "zero",
        "name"
    ],
    errors = "ignore"
    )

    #Handle missing values

    df["Age"] = df["Age"].fillna(df["Age"].median())
    df["Fare"] = df["Fare"].fillna(df["Fare"].median())
    df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

    #Convert categorical to numeric data[its type of one hot encoding]
    df = pd.get_dummies(
        df,
        columns =["Embarked"],
        drop_first= True,
        dtype = int
    )



    print(df.head())

    print("Data preprocessing completed")
    

    return df


#--------------------------------------------------------------
#
#   Function Name: main
#   Descritpion:   Entry point fun
#   Input :        None
#   Output:        None
#   Author:        Deep Jadhav
#   Date:          16/08/2026
#
#--------------------------------------------------------------
def main():
   #Step1
   df =  LoadData("MarvellousTitanicDataset.csv")
   #Step2
   df = PreprocessData(df)

if __name__ == "__main__":
    main()