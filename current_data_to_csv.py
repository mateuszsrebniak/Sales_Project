# This Python script connects to an Oracle database, 
# retrieves data for the current date from a specific table, 
# and saves the data to a CSV file.

import oracledb as orcl
from datetime import datetime
import pandas as pd
import os

# Oracle database connection settings
username = "Cleaning_Company"
password = "cleaning"
dsn = "XEPDB1"

# Establish connection to Oracle database
connection = orcl.connect(user=username, password=password, dsn=dsn)
cursor = connection.cursor()

# Get current date
current_date = str(datetime.now().date())

# SQL query to retrieve data for the current date
query = f"SELECT * FROM data_to_analyse WHERE realization_date = TO_DATE('{current_date}', 'YYYY-MM-DD')"
result_data_frame = pd.read_sql(query, connection)

# Define the path to the folder to store the file
folder_to_store_file_path = "C:/Users/Mateusz/OneDrive/Pulpit/Nauka/Python/Sales_Project/data_for_reports"

# Check if the folder exists; if not, create it
if not os.path.exists(folder_to_store_file_path):
    os.makedirs(folder_to_store_file_path)

# Define the CSV file name with the current date
csv_file_name = os.path.join(folder_to_store_file_path, f"orders_data_{current_date}.csv")

# Save the data to a CSV file
result_data_frame.to_csv(csv_file_name, index=False)