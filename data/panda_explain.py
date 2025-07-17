""""
panda
"""
"""panda is a powerful data manipulation and analysis library for Python.
It provides data structures like DataFrames and Series, which are designed for handling structured data efficiently.
Pandas is widely used for data analysis, cleaning, and transformation tasks."""

import pandas as pd
import numpy as np

data = pd.read_csv('Data.csv')
print(data)
print(data.describe())

# x = data.iloc[:, :-1].values
# y = data.iloc[:, -1].values

# from sklearn.impute import SimpleImputer

# simple_imputer_object = SimpleImputer(missing_values=np.nan, strategy='mean')
# simple_imputer_object.fit(x[:, 1:3])  # Fit only on numeric columns
# x[:,1:3] = simple_imputer_object.transform(x[:, 1:3])

# from sklearn.preprocessing import LabelEncoder 
# label_encoder_object = LabelEncoder()
# y = label_encoder_object.fit_transform(y)

# from sklearn.preprocessing import OneHotEncoder
# from sklearn.compose import ColumnTransformer
# column_transformer_object = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [0])], remainder='passthrough')
# X = np.array(column_transformer_object.fit_transform(x))

# from sklearn.model_selection import train_test_split    
# X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.2, random_state=42)

# from sklearn.linear_model import LogisticRegression
# logistic_regression_object = LogisticRegression(random_state=0)
# logistic_regression_object.fit(X_train, y_train)

# y_pred = logistic_regression_object.predict(X_test)

# from sklearn.metrics import confusion_matrix
# confusion_matrix_object = confusion_matrix(y_test, y_pred)
# print(confusion_matrix_object)