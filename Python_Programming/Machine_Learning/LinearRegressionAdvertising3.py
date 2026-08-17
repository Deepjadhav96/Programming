import numpy as np
import pandas as pd
import matplotlib as plt

from sklearn .linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

def MarvellousRegression(Datapath):
    border = "-"*40
    #Step1: Load the Data
    print(border)
    print("#Step1: Load the Data")
    print(border)

    df = pd.read_csv(Datapath)

    print(df.head())
    
    print(border)

    #Step2: Remove unwanted columns
    print(border)
    print("Step2: Remove unwanted columns")
    print(border)

    if "Unnamed: 0" in df.columns:
        df = df.drop(columns=["Unnamed: 0"])

    print(df.head())

    #Step3: Check missing values
    print(border)
    print("Step3: Check missing values")
    print(border)

    print("Total missing values: ")

    print(border)
    print(df.isnull().sum())
    print(border)


    #Step4:Statistical Summary 
    print(border)
    print("Step4: Statistical Summary")
    print(border)

    print(df.describe())

    print(border)




def main():
    MarvellousRegression("Advertising.csv")
if __name__ == "__main__":
    main()