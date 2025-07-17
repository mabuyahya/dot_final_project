"""
data
"""
"""Data is a collection of values or facts that represent information."""
# what is data?
"""it can be"""
"""Raw (unprocessed): "42", "2025-07-15", "John", 2.5"""
"""Structured (organized): Tables, CSV files, databases"""
"""Unstructured: Images, videos, text documents, audio"""

# type of data
"""By Format:"""
"""Structured Data: Easily stored in tables. E.g., SQL databases
Semi-structured: JSON, XML
Unstructured: PDFs, audio files, videos, emails"""
"""By Nature:"""
"""Quantitative: Numerical data (e.g., sales figures, temperatures)"""
"""Qualitative(categorical): Descriptive data (e.g., customer reviews, survey responses)"""

#  Lifecycle of Data (Data Pipeline)
"""Data Collection: Gathering data from various sources (e.g., sensors, databases, APIs)"""
"""Data Processing: Cleaning, transforming, and organizing data for analysis"""
"""Data Storage: Saving data in databases, data lakes, or files"""
"""Data Analysis: Extracting insights using statistical methods, machine learning, or data visualization"""

#What Is Machine Learning?
"""Machine Learning is a branch of AI where computers learn from data instead of being explicitly programmed."""
"""You’ve written rules like:
if hours > 3:
    grade = 90
else:
    grade = 70
In ML, you don’t write this rule — the machine figures it out automatically by looking at data."""

#What Is a Model?
"""A model is what gets created when the machine learns from data.
Training: Model learns from X and y
Prediction: Model uses what it learned to predict new y values
Think of it like a function: model(X) → y"""

"""Machine Learning is when you give the computer data instead of rules.
The computer uses algorithms to learn patterns (like if-else logic or formulas) from the data and builds a model.
That model acts like a function: you give it new inputs and it returns predictions based on what it learned."""






import pandas as pd #type:ignore
import numpy as np #type:ignore

data = pd.read_csv('Data.csv')
# print(data)
print(data.isnull().sum())
# print(data.info())
# print(data.describe())

"""first problem i have Nan values in the data"""
"""so i can fix it by using SimpleImputer from sklearn"""
"""or from pandas i can use fillna() method to fill NaN values or dropna() to remove them"""
"""but the pandas aproach is not recommended for large datasets"""
# using pandas to fill NaN values
# data['Age'] = data['Age'].fillna(data['Age'].mean())
# data['Salary'] = data['Salary'].fillna(data['Salary'].mean())
# print(data.isnull().sum())

# using SimpleImputer from sklearn to fill NaN values
from sklearn.impute import SimpleImputer

imputer_object = SimpleImputer(missing_values=np.nan, strategy='mean')
imputer_object.fit(data[['Age', 'Salary']])  # Fit only on numeric columns
data[['Age', 'Salary']] = imputer_object.transform(data[['Age', 'Salary']])
print(data.isnull().sum())

"""secand problem i have categorical data in the data"""
"""so i need to convert it to numerical data"""
"""i can use LabelEncoder from sklearn to convert categorical data to numerical data"""
from sklearn.preprocessing import LabelEncoder
label_encoder_object = LabelEncoder()
data['Country'] = label_encoder_object.fit_transform(data['Country'])
data['Purchased'] = label_encoder_object.fit_transform(data['Purchased'])
# print(data)
"""but the problem with LabelEncoder is that it assigns arbitrary numerical values to categories, which can mislead some algorithms"""
"""maybe some algorithms will think that 'France' is greater than 'Spain' because it has a higher numerical value"""
"""so i can use OneHotEncoder from sklearn to convert categorical data to numerical data without losing information"""
"""the OneHotEncoder creates a binary column for each category, which is more suitable for many machine learning algorithms"""
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
column_transformer_object = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), ['Country'])], remainder='passthrough')
# print(data)
data = pd.DataFrame(column_transformer_object.fit_transform(data))
# print(data)

"""now i have a numerical data and i can use it for machine learning algorithms"""
"""but before that i need to split the data into training and testing sets"""
from sklearn.model_selection import train_test_split
X = data.iloc[:, :-1].values
Y = data.iloc[:, -1].values
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

"""now i can use the training set to train a machine learning model"""
