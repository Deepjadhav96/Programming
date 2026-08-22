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

    #Step4: Elbow method
    WCSS = []

    for k in range(1,11):
        model = KMeans(
            n_clusters= k,
            random_state= 42,
            n_init= 10
        )
        model.fit(X_scaled)
        WCSS.append(model.inertia_)

    print("Values of WCSS :")
    for i in range(len(WCSS)):
        print(f"{i+1} : {WCSS[i]}")

    #Step5:Visualisation

    plt.plot(range(1,11),WCSS,marker = 'o')
    plt.xlabel("Number of clusters i.e k")
    plt.ylabel("WCSS")
    plt.title("Marvellous Elbow method")
    plt.grid()
    plt.show()

    #Step6: Final model 
    model = KMeans(
                n_clusters= 4,
                random_state= 42,
                n_init= 10
            )
    clusters = model.fit_predict(X_scaled)

    df["Cluster"] = clusters

    print("Dataset with clusters :")
    print(df.head(20))


if __name__ == "__main__":
    main()