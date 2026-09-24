#--------------------------------------------------------
#   Deep Learning
#--------------------------------------------------------
#   1. Read the Data from csv
#   2. Data Analysis (EDA)
#   3. Preprocessing
#   4. Train Test Split
#   5. Feature Scaling
#   6. FNN model training
#   7. Model evaluation
#   8. Graphical representation
#   9. Model Preserve
#  10. Model loading and Preserve 
#  11. Test unseen data
#--------------------------------------------------------
import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import confusion_matrix,accuracy_score

border = "-"*40
#--------------------------------------------------------
#       Step1: Data loading
#--------------------------------------------------------
print(border)
print("# Step1: Data loading")

data = pd.read_csv("placement_data.csv")

print("Complete Dataset: ")
print(data)

#----------------------------------------------------
#  2. Data Analysis (EDA)
#----------------------------------------------------

print("First 5 rows:")
print(data.head())

print("Column name:")
print(data.columns)

print("Shape of Dataset: ")
print(data.shape)

print("Statistical summary :")
print(data.describe())


#----------------------------------------------------
#  3.Preprocessing
#----------------------------------------------------

print("3.Preprocessing")

X = data[['Aptitude','Coding','Communication','Academics','Internship']]
Y = data['Placed']

print("Input features :")
print(X.head())

print("Target:")
print(Y.head())


#----------------------------------------------------
# 4. Train test split
#----------------------------------------------------

print("# 4. Train test split")

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.3,random_state=42)

print("Training input shape: ",X_train.shape)
print("Testing input shape: ",X_test.shape)
print("Training output shape: ",Y_train.shape)
print("Testig output shape: ",Y_test)


#----------------------------------------------------
# 5: Feature scaling
#----------------------------------------------------

print("# 5: Feature scaling")

scalar = StandardScaler()

X_train_scaled = scalar.fit_transform(X_train)
X_test_scaled =  scalar.fit_transform(X_test)

print("Scaled training data: ")
print(X_train_scaled[:5])

#----------------------------------------------------
# 6.FNN model training
#----------------------------------------------------

print("6 : FNN model training")

model = MLPClassifier(
    hidden_layer_sizes=(8,4),
    activation='relu',
    solver='adam',
    max_iter=1000,
    random_state=42
)

print(model)


model = model.fit(X_train_scaled,Y_train)
print("Model training completed")


#----------------------------------------------------
#   7. Model evaluation
#----------------------------------------------------

print("7.Model evaluation")

Y_pred = model.predict(X_test_scaled)

accuracy = accuracy_score(Y_test,Y_pred)
print("Accuracy score: ")
print(accuracy)

cm = confusion_matrix(Y_test,Y_pred)

print("Confusion matrix: ",cm)

print("Predict the probability: ")

Y_prob = model.predict_proba(X_test_scaled)

print(Y_prob[:5])

#----------------------------------------------------
#   9. Model Preserve
#----------------------------------------------------

print("9. Model Preserve")
joblib.dump(model,"placement_fnn_model.pkl")
joblib.dump(scalar,"placement_scaler.pkl")

print("Model and Scaler gets dumped successfully")


#----------------------------------------------------
#   10. Model loading and preserve
#----------------------------------------------------

print("10. Model loading and preserve")

loaded_model = joblib.load("placement_fnn_model.pkl")
loaded_scaler = joblib.load("placement_scaler.pkl")

print("Model gets loaded successfully")


#----------------------------------------------------
#  11. Test unseen data
#  Aptitude :       70
#  Coding:          75
#  Communication:   80
#  Academics:       85
#  Internship:      1
#----------------------------------------------------

print("11. Test unseen data")

new_student = pd.DataFrame([[70,75,80,85,1]],columns=['Aptitude','Coding','Communication','Academics','Internship'])

new_student_scaled = loaded_scaler.transform(new_student)

new_prediction = loaded_model.predict(new_student_scaled)

new_probabilty = loaded_model.predict_proba(new_student_scaled)

print("New Student Data:")
print(new_student)

print("Prediction probability:",new_probabilty)

if(new_prediction[0] == 1):
    print("Predictipon: Placed")
else:
    print("Predictipon: Not Placed")
