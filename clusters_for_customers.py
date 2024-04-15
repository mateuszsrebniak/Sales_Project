import pandas as pd
import sys
sys.path.append("c:\\Users\\Mateusz\\OneDrive\\Pulpit\\Nauka\\Python\\Sales_Project\\.venv\\Lib\\site-packages")
import mysql.connector
# from sklearn.cluster import KMeans

# Ustawienia połączenia z bazą danych Oracle
username = "root"
password = "admin"
host = "localhost"
database = "Cleaning_Company"

# Establish a connection to the MySQL database
connection = mysql.connector.connect(user=username, password=password, host=host, database=database)
query = f"SELECT * FROM orders_with_costs;"
result_data_frame = pd.read_sql(query, connection)

print(result_data_frame.head())