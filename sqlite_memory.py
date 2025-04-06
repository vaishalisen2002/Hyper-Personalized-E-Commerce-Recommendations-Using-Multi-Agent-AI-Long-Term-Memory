import sqlite3
from typing import Any, List, Dict
import pandas as pd

class SQLiteMemory:
    def __init__(self, db_path: str = "memory.db"):
        self.db_path = db_path
        self.init_database()

    def init_database(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS user_context (
                    Customer_ID INTEGER PRIMARY KEY,
                    context TEXT NOT NULL
                )
            """)
            conn.execute("""
                CREATE TABLE IF NOT EXISTS products (
                    Product_ID INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    description TEXT,
                    metadata TEXT
                )
            """)
            self.load_data_from_csv('customer_data_collection.csv', 'user_context')
            self.load_data_from_csv('product_recommendation_data.csv', 'products')

    def executeSQL(self, query: str) -> List[Dict[str, Any]]:
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.execute(query)
            results = cursor.fetchall()
            return [dict(row) for row in results]

    def load_data_from_csv(self, csv_path: str, table_name: str):
        df = pd.read_csv(csv_path)
        with sqlite3.connect(self.db_path) as conn:
            df.to_sql(table_name, conn, if_exists='replace', index=False) 