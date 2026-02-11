import sqlite3
import os

def initialize_db(db_name: str = "crypto_pipeline.db", schema_file: str ="schema.sql") -> None:
    """Creates the database and tables using the schema file."""
    
    if not os.path.exists(schema_file):
        raise FileNotFoundError(f"Schema file \"{schema_file}\" not found.")
    
    with open(schema_file, "r") as schema:
        schema_sql = schema.read()
    
    try:
        with sqlite3.connect(db_name) as conn:
            cursor = conn.cursor()
            cursor.executescript(schema_sql) # Create Tables
            print("Database initialized successfully.")
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        conn.close() # To make sure.

if __name__ == "__main__":
    initialize_db()