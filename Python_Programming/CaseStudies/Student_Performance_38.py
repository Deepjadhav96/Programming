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

print("Last 5 entries from Dataset are:")
print(df.tail())

print("Total numbers of rows and columns :")
print(df.shape)

################################################
#         Step2: Data analysis[EDA]
################################################


print(Border)
print("Step2: Data analysis[EDA]")
print(Border)

print("Total number of students in Dataset: ",df["FinalResult"].shape)

print("Shape of Dataset :", df.shape)

print("Columns names :",list(df.columns))

print("Data type of each columns:")
for i in df.columns:
    print(i," ",df[i].dtype)

print("Count of passed students: ",(df["FinalResult"]== 1).sum())

print("Count of failed students: ",(df["FinalResult"]==0).sum())

print("Average of StudyHours :",df["StudyHours"].mean())
print("Average of Attendence :",df["Attendance"].mean())
print("Maximum of PreviousScore :",df["PreviousScore"].max())
print("Minimum of SleepHours :",df["SleepHours"].min())

print("Missing values per columns :",df.isnull().sum())

print("Class Distribution [Final result]")
print(df["FinalResult"].value_counts())

print("Calculate of passed and failed students:")

count_passed = ((df["FinalResult"]== 1).sum()) 
count_failed = ((df["FinalResult"]== 0).sum() )
print("Percentage of passed students: ",(count_passed/df["FinalResult"].shape)*100)
print("Percentage of failed students: ",(count_failed/df["FinalResult"].shape)*100)

################################################
#         Step3: Data visualisation
################################################
print(Border)
print("Step3: Data visualisation")
print(Border)

plt.hist(
    df["StudyHours"],
    bins = 5,
    edgecolor = "black",
    alpha = 0.8,
    rwidth = 0.9
)

plt.title("Marvellous Study Hours")
plt.xlabel("Study Hours")
plt.ylabel("Numbers of students")
plt.show()

plt.scatter(
    df["StudyHours"],
    df["PreviousScore"],
    s=100,
    marker="o",
    alpha=0.8,
    edgecolors="black",
    linewidth=1,
    label = "Students"
)
plt.title("Marvellous Study Hours")
plt.xlabel("Study Hours")
plt.ylabel("Previous Score")

plt.grid(True)
plt.legend()

plt.show()

plt.boxplot(
    df["Attendance"],
    notch = True,

)

plt.title("Customized Box Plot")
plt.show()