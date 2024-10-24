"""
Module 1: data_loading.py
Load data from SQL database using SQLite3
"""

import sqlite3
import pandas as pd


DB_PATH = r'C:\Users\girli\OneDrive\Desktop\Projekt_Data_Science\Final\birthrate_education_costs.db'

def load_data(db_path):
    """
    Load data from SQLite database into DataFrames.

    Args:
        db_path (str): Path to the SQLite database.

    Returns:
        dict: A dictionary of DataFrames for each table.
    """
    try:
        conn = sqlite3.connect(db_path)
        tables = {
            'birth_data': pd.read_sql("SELECT * FROM birth_data_per_region", conn),
            'mortality_data': pd.read_sql("SELECT * FROM mortality_data_per_region", conn),
            'migration_data': pd.read_sql("SELECT * FROM migration_data", conn),
            'population_0_16': pd.read_sql("SELECT * FROM population_0_16_years", conn),
            'population_17_19': pd.read_sql("SELECT * FROM population_17_19_years", conn),
            'grundskola_costs': pd.read_sql("SELECT * FROM grundskola_costs_per_child"),
            'gymnasieskola_costs': pd.read_sql("SELECT * FROM gymnasieskola_costs_per_child")
        }
        print(tables).head()
    except sqlite3.Error as e:
        print(f"An error occurred while connecting to the database: {e}")
        return None
    finally:
        if conn:
            conn.close()

    return tables
