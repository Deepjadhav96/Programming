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

#Step3: Data preprocessing
#--------------------------------------------------------------
#
#   Function Name: splitData
#   Descritpion:   It Performs spliting activity
#   Input :        DataFrame
#   Output:        4 subset for training and testing
#   Author:        Deep Jadhav
#   Date:          16/08/2026
#
#--------------------------------------------------------------

def splitData(df):
    X = df.drop("Survived",axis = 1)
    Y = df["Survived"]

    X_train,X_test,Y_train,Y_test = train_test_split(
        X,
        Y,
        test_size= 0.2,
        random_state= 42
    )
    print("Dataset splitting completed successfully")
    return  X_train,X_test,Y_train,Y_test

#Step4: Training model
#--------------------------------------------------------------
#
#   Function Name: TrainModel
#   Descritpion:   It Performs model training
#   Input :        Training features and labels
#   Output:        Trained model
#   Author:        Deep Jadhav
#   Date:          16/08/2026
#
#--------------------------------------------------------------

def TrainModel(X_train, Y_train):
    model = LogisticRegression(max_iter=1000)
    model = model.fit(X_train, Y_train)

    print("Model trainde successfully")

    return model

#Step5: Evaluate model
#--------------------------------------------------------------
#
#   Function Name: EvaluateModel
#   Descritpion:   It Performs model testing
#   Input :        Model , Testing Data(features, labels)
#   Output:        none
#   Author:        Deep Jadhav
#   Date:          16/08/2026
#
#--------------------------------------------------------------
def EvaluateModel(model , X_test, Y_test):
    Y_pred = model.predict(X_test)

    accuracy = accuracy_score(Y_test, Y_pred)

    print("Accuracy :",accuracy)
    print("Confusion matrix :")
    print(confusion_matrix(Y_test, Y_pred))

#Step6: Preserved model
#--------------------------------------------------------------
#
#   Function Name: PreservedModel
#   Descritpion:   It Performs model preservation into .pkl file
#   Input :        Model 
#   Output:        none
#   Author:        Deep Jadhav
#   Date:          16/08/2026
#
#--------------------------------------------------------------
def PreservedModel(model,filename):
    joblib.dump(model,filename)

    print("Model preserved with : ",filename)



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

   #Step3:
   X_train,X_test,Y_train,Y_test = splitData(df)

   #Step4:
   model = TrainModel(X_train, Y_train)

   #Step5:
   EvaluateModel(model,X_test,Y_test)

   #Step6:
   PreservedModel(model,"MarvellousTitanic.pkl")
if __name__ == "__main__":
    main()

