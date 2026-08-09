import pandas as pd
import matplotlib.pyplot as plt

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.preprocessing import StandardScaler


def MarvellousClassifier(DataPath):
    border = "-"*40

    #Step1 : Load the dataset from CSV file
    print(border)
    print("Step1 : Load the dataset from CSV file")
    print(border)

    df = pd.read_csv(DataPath)

    print(border)
    print("Some entries from dataset:")
    print(df.head())
    print(border)

    #step2: Clean the dataset
    print(border)
    print("Step2 : Clean the dataset")
    print(border)

    df.dropna(inplace=True)
    print("Shape of Dataset : ",df.shape)
    print("Total records : ",df.shape[0])
    print("Total columns : ",df.shape[1])

    print(border)

    #Step3:Separate Independent and Dependent variables
    print(border)
    print("Step3:Separate Independent and Dependent variables")
    print(border)

    X = df.drop(columns=['Class'])
    Y = df['Class']

    print("Shape of X : ",X.shape)
    print("Shape of Y : ",Y.shape)

    print(border)
    print("Input columns : ",X.columns.tolist())
    print("Output columns : Class")
    print(border)

    #step4:Split the dataset for training and testing
    print(border)
    print("step4:Split the dataset for training and testing")
    print(border)

    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42,stratify=Y)

    print(border)
    print("Details of training and testing data ")
    print("Shape of X_train :",X_train.shape)
    print("Shape of X_train :",X_test.shape)

    print("Shape of X_train :",Y_train.shape)
    print("Shape of X_train :",Y_test.shape)


def main():
    MarvellousClassifier("WinePredictor.csv")
if __name__ == "__main__":
    main()