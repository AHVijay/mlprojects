import pandas as pd
from sklearn.model_selection import train_test_split

class DataIngestion:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_data(self):
        """Load data from a CSV file."""
        try:
            data = pd.read_csv(self.file_path)
            print("[INFO] Data loaded successfully.")
            return data
        except Exception as e:
            raise Exception(f"Error loading data: {e}")

    def validate_data(self, df):
        """Validate the data for missing values."""
        if df.isnull().sum().any():
            raise ValueError("Data contains missing values")
        print("[INFO] Data validation passed.")

    def split_data(self, df, target_column):
        """Split the data into training and testing sets."""
        X = df.drop(columns=[target_column])
        y = df[target_column]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        print("[INFO] Data split into training and testing sets.")
        return X_train, X_test, y_train, y_test

    def save_data(self, df, output_path):
        """Save the processed data to a file."""
        df.to_csv(output_path, index=False)
        print(f"[INFO] Data saved to {output_path}.")
