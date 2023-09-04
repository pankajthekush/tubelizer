import pandas as pd
from .db_operations import create_db_and_insert_data

def read_data(file_path, chunk_size=50000):
    if_exists = "replace"
    for chunk in pd.read_csv(file_path, chunksize=chunk_size):
        if chunk.shape[1] > 100:
            raise ValueError("CSV file has more than 100 columns.")
        create_db_and_insert_data(chunk, if_exists=if_exists)
        if_exists = "append"
