import os
import sqlite3
import pandas as pd

def list_databases(listbox):
    db_files = [f for f in os.listdir('.') if f.endswith('.db')]
    listbox.delete(0, tk.END)
    for db in db_files:
        listbox.insert(tk.END, db)

def create_db_and_insert_data(chunk, db_name="csv_data.db", if_exists="replace"):
    conn = sqlite3.connect(db_name)
    chunk.to_sql("csv_table", conn, if_exists=if_exists, index=False)
    conn.commit()
    conn.close()

def read_data(file_path, chunk_size=50000):
    if_exists = "replace"
    for chunk in pd.read_csv(file_path, chunksize=chunk_size):
        if chunk.shape[1] > 100:
            raise ValueError("CSV file has more than 100 columns.")
        create_db_and_insert_data(chunk, if_exists=if_exists)
        if_exists = "append"
