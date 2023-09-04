import pandas as pd
import os
from .db_operations import create_db_and_insert_data


def create_db_name(file_path):
    if not file_path.lower().endswith('.csv'):
        return "Error: Not a CSV file"
    base_filename = os.path.splitext(os.path.basename(file_path))[0]
    cleaned_filename = ''.join(c if c.isalnum() else '_' for c in base_filename)
    db_name = cleaned_filename + '.db'
    return db_name



def read_data(file_path, chunk_size=50000):
    if_exists = "replace"
    for chunk in pd.read_csv(file_path, chunksize=chunk_size):
        if chunk.shape[1] > 100:
            raise ValueError("CSV file has more than 100 columns.")
        db_name = create_db_name(file_path=file_path)
        create_db_and_insert_data(chunk, db_name=db_name,if_exists=if_exists)
        if_exists = "append"
    return db_name
