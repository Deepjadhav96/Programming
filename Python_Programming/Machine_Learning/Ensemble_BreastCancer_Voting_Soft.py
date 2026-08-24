import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score,confusion_matrix

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier

from sklearn.ensemble import VotingClassifier

#--------------------------------------------------------------
#   Step1: Import the dataset
#--------------------------------------------------------------
df = pd.read_csv("breast_cancer.csv")

print("Shape of Dataset: ",df.shape)

print("First few rows :")
print(df.head())


#--------------------------------------------------------------
#   Step2: Separate features and labels
#--------------------------------------------------------------

X = df.drop("target",axis = 1)
Y = df["target"]

print("X shape: ",X.shape)
print("Y shape: ",Y.shape)


#--------------------------------------------------------------
#   Step3: Split the dataset for training and testing 
#--------------------------------------------------------------

X_train,X_test,Y_train,Y_test = train_test_split(
                                                X,
                                                Y,
                                                test_size=0.2,
                                                random_state=42
                                                )


#--------------------------------------------------------------
#   Step4: Scale the features
#--------------------------------------------------------------

scalar = StandardScaler()

X_train = scalar.fit_transform(X_train)
X_test = scalar.fit_transform(X_test)


#--------------------------------------------------------------
# Step5.1: Create the Individual models
#--------------------------------------------------------------

model_log = LogisticRegression(max_iter= 1000)



model_det = DecisionTreeClassifier(random_state= 42)


model_knn = KNeighborsClassifier(n_neighbors= 5)

#--------------------------------------------------------------
# Step5.2: Create the voting model
#--------------------------------------------------------------
model = VotingClassifier(
                    estimators=[
                        ('logistic',model_log),
                        ('decision_tree',model_det),
                        ('knn',model_knn)
                    ],
                    voting= 'soft'
)
#--------------------------------------------------------------
#   Step6: Train the model
#--------------------------------------------------------------

model = model.fit(X_train, Y_train)


#--------------------------------------------------------------
#   Step7: Test the model
#--------------------------------------------------------------

Y_pred = model.predict(X_test)


#--------------------------------------------------------------
#   Step8: Evaluate the model
#--------------------------------------------------------------

print("Accuracy : ",accuracy_score(Y_test,Y_pred))

print("Confusion matrix : ")
print(confusion_matrix(Y_test,Y_pred))

