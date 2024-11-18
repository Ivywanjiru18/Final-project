#Using panda librabry for data manipulation

import pandas as pd

# Load data from a CSV file
data = pd.read_csv('health_data.csv')

# Display the first few rows of the DataFrame
print(data.head())

# Data manipulation: Filter data for a specific condition
filtered_data = data[data['activity_level'] > 5]

# Group by a specific column and calculate the mean
mean_values = filtered_data.groupby('user_id').mean()
print(mean_values)

#Using numPy for numerical operations

import numpy as np

# Create a NumPy array
activity_levels = np.array(data['activity_level'])

# Calculate basic statistics
mean_activity = np.mean(activity_levels)
std_activity = np.std(activity_levels)

print(f'Mean Activity Level: {mean_activity}')
print(f'Standard Deviation of Activity Levels: {std_activity}')

#Using SciKit-learn for predictive modelling


from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Prepare the features (X) and target variable (y)
X = data[['feature1', 'feature2']]  # Replace with actual feature names
y = data['target_variable']           # Replace with actual target variable name

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a linear regression model
model = LinearRegression()

# Fit the model on the training data
model.fit(X_train, y_train)

# Make predictions on the test set
predictions = model.predict(X_test)

# Display predictions
print(predictions)

#Thresholds for vital signs by using the panda library

import pandas as pd

# Sample incoming data (you would typically fetch this from a database or API)
data = {
    'user_id': [1, 2, 3],
    'heart_rate': [85, 110, 58],
    'blood_pressure': ['120/80', '135/85', '150/95'],
    'creatinine': [0.9, 1.5, 0.7]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Function to analyze heart rate
def analyze_heart_rate(hr):
    if hr < 60:
        return "Bradycardia"
    elif hr > 100:
        return "Tachycardia"
    else:
        return "Normal"

# Function to analyze blood pressure
def analyze_blood_pressure(bp):
    systolic, diastolic = map(int, bp.split('/'))
    if systolic < 120 and diastolic < 80:
        return "Normal"
    elif systolic < 130 and diastolic < 80:
        return "Elevated"
    elif systolic < 140 or diastolic < 90:
        return "Hypertension Stage 1"
    else:
        return "Hypertension Stage 2"

# Function to analyze creatinine levels
def analyze_creatinine(creatinine):
    if creatinine > 1.2:
        return "Elevated"
    else:
        return "Normal"

# Apply analysis functions to the DataFrame
df['heart_rate_status'] = df['heart_rate'].apply(analyze_heart_rate)
df['blood_pressure_status'] = df['blood_pressure'].apply(analyze_blood_pressure)
df['creatinine_status'] = df['creatinine'].apply(analyze_creatinine)

# Display the results
print(df[['user_id', 'heart_rate', 'heart_rate_status', 
           'blood_pressure', 'blood_pressure_status', 
           'creatinine', 'creatinine_status']])