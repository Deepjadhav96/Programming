import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split

from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report
)
Border = "-"*40

#################################################
##          Step 1: Load the Dataset.
#################################################

print(Border)
print("Step 1: Load the Dataset.")
print(Border)

Datapath = "student_performance_ml.csv"

df = pd.read_csv(Datapath)

print("Dataset loaded successfully")

print("Initial entries from Dataset are:")
print(df.head())

#################################################
##         Step2: Data analysis[EDA]
#################################################


print(Border)
print("Step2: Data analysis[EDA]")
print(Border)

print("Shape of Dataset :", df.shape)

print("Columns names :",list(df.columns))

print("Missing values per columns :",df.isnull().sum())

print("Class Distribution [Final result]")
print(df["FinalResult"].value_counts())

print("Statical report of dataset:")
print(df.describe())

#######################################################
## Step3: Decides Independent and Dependent variable
#######################################################

print(Border)
print("Step2: Decides Independent and Dependent variable")
print(Border)

#X : Independent variable / Features
#Y : Dependent variable / Labels

feature_cols = [
    "StudyHours",
    "Attendance",
    "PreviousScore",
    "AssignmentsCompleted",
    "SleepHours",
]

X = df[feature_cols]
Y = df["FinalResult"]

print("X shape : ",X.shape)
print("Y shape : ",Y.shape)

#######################################################
## Step4: Visualisation of Dataset.
#######################################################

print(Border)
print("Step4: Visualisation of Dataset")
print(Border)

#Scatterplot
# plt.figure(figsize=(7,5))

# for sp in df["StudyHours"].unique():
#     temp = df[df["StudyHours"]==sp]
#     plt.scatter(temp[])


#######################################################
## Step 5: Split the Dataset for training and testing.
#######################################################

print(Border)
print("Step 5: Split the Dataset for training and testing.")
print(Border)

X_train,X_test,Y_train,Y_test = train_test_split(X, Y, test_size = 0.5,random_state = 42)

print("Dataset splitting activity done")

print("X shape :",X.shape)
print("Y shape :",Y.shape)

print("X_train :",X_train.shape)
print("X_test : ",X_test.shape)

print("Y_train :",Y_train.shape)
print("Y_test :",Y_test.shape)


#######################################################
#   Step6: Build the model
#######################################################
print(Border)
print("Step6: Build the model")
print(Border)

model = DecisionTreeClassifier(max_depth=5)

print("Model gets created successfully")

#######################################################
#   Step7: Train the model
#######################################################

print(Border)
print("Step7: Train the model")
print(Border)

model.fit(X_train, Y_train)

print("Model train successfully")

#######################################################
#   Step8: Test the model
#######################################################

print(Border)
print("Step8: Test the model")
print(Border)

Y_pred = model.predict(X_test)

print("Model testing done")

print("Expected answer:")
print(Y_test)

print("Predicted answer")
print(Y_pred)

#######################################################
# Step 9: Evaluate the model
#######################################################

print(Border)
print("Step 9: Evaluate the model")
print(Border)

accuracy = accuracy_score(Y_test, Y_pred)

print("Accuracy of model is: ",accuracy*100)

#######################################################
#Visualization is missing
#######################################################
