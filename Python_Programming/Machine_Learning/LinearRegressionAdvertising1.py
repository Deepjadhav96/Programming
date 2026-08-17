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





def main():
    MarvellousRegression("Advertising.csv")
if __name__ == "__main__":
    main()