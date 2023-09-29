import tkinter as tk
from tkinter import Label, Entry, Button
import seaborn as sns
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import warnings

# Load the Titanic dataset
titanic = sns.load_dataset("titanic")
titanic.to_csv("titanic.csv", index=False)

# Load the Titanic dataset from the CSV file
data = pd.read_csv("titanic.csv")

# Data preprocessing
data['sex'] = data['sex'].map({'female': 0, 'male': 1})
data['age'].fillna(data['age'].median(), inplace=True)
data = data[['pclass', 'sex', 'age', 'parch', 'fare', 'survived']]

# Split the dataset into features (X) and target (y)
X = data.drop('survived', axis=1)
y = data['survived']

# Suppress warnings
warnings.filterwarnings("ignore", category=UserWarning)

# Train a Random Forest classifier
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X, y)

# Create a Tkinter window
window = tk.Tk()
window.title("Titanic Survival Predictor")

# Function to make predictions and display the result
def predict_survival():
    pclass = int(class_entry.get())
    sex = int(gender_var.get())
    age = float(age_entry.get())
    parch = int(parch_entry.get())
    fare = float(fare_entry.get())
    
    input_data = np.array([[pclass, sex, age, parch, fare]])
    prediction = clf.predict(input_data)
    
    if prediction[0] == 1:
        result_label.config(text="Survived")
    else:
        result_label.config(text="Did not survive")

# Rest of your GUI code remains the same
# ...




# Create and configure GUI elements
class_label = Label(window, text="Passenger Class (1, 2, or 3):")
class_entry = Entry(window)

gender_label = Label(window, text="Gender (0 for female, 1 for male):")
gender_var = tk.StringVar()
gender_var.set("1")
gender_option = tk.OptionMenu(window, gender_var, "0", "1")

age_label = Label(window, text="Age:")
age_entry = Entry(window)

sibsp_label = Label(window, text="Number of Siblings/Spouses Aboard:")
sibsp_entry = Entry(window)

parch_label = Label(window, text="Number of Parents/Children Aboard:")
parch_entry = Entry(window)

fare_label = Label(window, text="Fare:")
fare_entry = Entry(window)

predict_button = Button(window, text="Predict Survival", command=predict_survival)

result_label = Label(window, text="Result will appear here")

# Arrange GUI elements using grid layout
class_label.grid(row=0, column=0, padx=10, pady=5)
class_entry.grid(row=0, column=1, padx=10, pady=5)

gender_label.grid(row=1, column=0, padx=10, pady=5)
gender_option.grid(row=1, column=1, padx=10, pady=5)

age_label.grid(row=2, column=0, padx=10, pady=5)
age_entry.grid(row=2, column=1, padx=10, pady=5)

sibsp_label.grid(row=3, column=0, padx=10, pady=5)
sibsp_entry.grid(row=3, column=1, padx=10, pady=5)

parch_label.grid(row=4, column=0, padx=10, pady=5)
parch_entry.grid(row=4, column=1, padx=10, pady=5)

fare_label.grid(row=5, column=0, padx=10, pady=5)
fare_entry.grid(row=5, column=1, padx=10, pady=5)

predict_button.grid(row=6, columnspan=2, padx=10, pady=10)
result_label.grid(row=7, columnspan=2, padx=10, pady=5)

window.mainloop()
