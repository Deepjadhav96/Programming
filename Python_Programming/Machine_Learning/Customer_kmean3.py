import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans


def main():

    #Step1: Load the Dataset
    df = pd.read_csv("Mall_Customers.csv")

    print("Dataset loaded with values")

    print(df.head())

    print("Missing values : ")
    print(df.isnull().sum())

    #Step2:Features selection
    X = df[["AnnualIncome","SpendingScore"]]

    print("Selected features :")
    print(X.head())

    #Step3: Scale the data
    scalar = StandardScaler()

    X_scaled = scalar.fit_transform(X)

    print("Scaled Data:")
    print(X_scaled[:5])


if __name__ == "__main__":
    main()