import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Sample Data
data = pd.DataFrame({
    'Age': [25, 30, 45, 22, 35],  # Numerical
    'Salary': [50000, 60000, 80000, 30000, 70000],  # Numerical
    'Country': ['India', 'USA', 'USA', 'India', 'UK'],  # Categorical
    'Purchased': [1, 0, 1, 0, 1]  # Target variable
})

# Defining feature columns
numerical_features = ['Age', 'Salary']
categorical_features = ['Country']

# Creating transformers for preprocessing
numerical_transformer = StandardScaler()
categorical_transformer = OneHotEncoder(handle_unknown='ignore')

# ColumnTransformer to apply different transformations to different features
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numerical_transformer, numerical_features),
        ('cat', categorical_transformer, categorical_features)
    ]
)

# Creating the full pipeline with preprocessing and model
model_pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('classifier', LogisticRegression())
])

# Splitting data
X = data.drop(columns=['Purchased'])
y = data['Purchased']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Fitting the pipeline
model_pipeline.fit(X_train, y_train)

# Making predictions
predictions = model_pipeline.predict(X_test)

print("Predictions:", predictions)
