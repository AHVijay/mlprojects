import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from typing import Tuple
from src.components.data_transformation import DataTransformationConfig
from src.components.data_transformation import DataTransformation

@dataclass
class DataIngestionConfig:
    """
    Data Ingestion Configuration
    """
    train_data_path: str = os.path.join('artifacts', 'train.csv')
    test_data_path: str = os.path.join('artifacts', 'test.csv')
    raw_data_path: str = os.path.join('artifacts', 'data.csv')

class DataIngestion:
    
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
        
    def initiate_data_ingestion(self):
        """
        Method to initiate data ingestion
        """
        logging.info("Data Ingestion started")
        
        try:
            # Read the data from the source (CSV file)
            df = pd.read_csv('notebook/data/stud.csv')
            
            # Create directories if they don't exist
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)
            
            # Save the raw data to a CSV file
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)
            
            # Split the data into train and test sets
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
            logging.info("Train and Test data split completed")
            
            # Save the train and test sets to CSV files
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)
            
            logging.info("Data Ingestion completed")
            
            return (
                self.ingestion_config.train_data_path, 
                self.ingestion_config.test_data_path
            )
        
        except Exception as e:
            raise CustomException(e, sys) from e
        
if __name__ == "__main__":
    data_ingestion = DataIngestion()
    data_ingestion.initiate_data_ingestion()