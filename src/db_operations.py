import sqlite3
import pandas as pd

def create_db_and_insert_data(chunk, db_name, if_exists="replace"):
    conn = sqlite3.connect(db_name)
    chunk.to_sql("csv_table", conn, if_exists=if_exists, index=False)
    conn.commit()
    conn.close()

def get_total_rows(db_name="csv_data.db", table_name="csv_table"):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
    total_rows = cursor.fetchone()[0]
    conn.close()
    return total_rows

def fetch_data_from_db(start, end, db_name="csv_data.db"):
    conn = sqlite3.connect(db_name)
    query = f"SELECT * FROM csv_table LIMIT {start}, {end}"
    subset = pd.read_sql_query(query, conn)
    conn.close()
    return subset
