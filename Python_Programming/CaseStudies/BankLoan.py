# Step1: Read the Data from CSV
# Step2: Data Analysis [EDA]
# Step3: Preprocessing
# Step4: Train test split
# Step5: Feature scaling
# Step6: FNN model trainig
# Step7: Model evaluation.



import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import confusion_matrix,accuracy_score

border = "-"*40

#------------------------------------------------------------------------------
# Step1: Data loading
#------------------------------------------------------------------------------

print(border)
print("Step1: Data loading")
print(border)

data = pd.read_csv("Loan_Default.csv")

print("Complete Dataset")
print(data)

#------------------------------------------------------------------------------
# Step2: Data Analysis(EDA)
#------------------------------------------------------------------------------
print(border)
print("Step2: Data Analysis(EDA)")
print(border)

print("First 5 rows: ")
print(data.head())

print("Column name: ")
print(data.columns)

print("Shape of Dataset:")
print(data.shape)

print("Statistical summary")
print(data.describe)

#----------------------------------------------------
#  Step3: Preprocessing
#----------------------------------------------------
print(border)
print("Step3: Preprocessing")
print(border)

X = data[['Income', 'LoanAmount', 'CreditScore', 'EmploymentYears',
       'ExistingLoans', 'MonthlyDebt', 'LoanTerm', 'PreviousDefault',
       'HomeOwnership']]

Y = data['Default']

print("Input features : ")
print(X.head())

print("Target:")
print(Y.head())

#----------------------------------------------------
#      Step4: Train Test Split
#----------------------------------------------------
