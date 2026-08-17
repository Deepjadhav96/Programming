import pandas as pd
import numpy as np
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score ,confusion_matrix

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
    LoadData("MarvellousTitanicDataset.csv")
if __name__ == "__main__":
    main()