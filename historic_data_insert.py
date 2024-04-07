# This Python script inserts data from CSV files into a MySQL database for a Cleaning Company project.

import sys
sys.path.append("c:\\Users\\Mateusz\\OneDrive\\Pulpit\\Nauka\\Python\\Sales_Project\\.venv\\Lib\\site-packages")
import csv
import mysql.connector

# Database connection settings
username = "root"
password = "admin"
host = "localhost"
database = "Cleaning_Company"

# Paths to CSV files
csv_paths = {
    "customers": "C:/Users/Mateusz/OneDrive/Pulpit/Nauka/Python/Sales_Project/historic_data/Customer.csv",
    "orders": "C:/Users/Mateusz/OneDrive/Pulpit/Nauka/Python/Sales_Project/historic_data/Order.csv",
    "workers": "C:/Users/Mateusz/OneDrive/Pulpit/Nauka/Python/Sales_Project/historic_data/Salesman.csv",
    "cleaningVariants": "C:/Users/Mateusz/OneDrive/Pulpit/Nauka/Python/Sales_Project/historic_data/CleaningVariant.csv"
}

# Establish a connection to the MySQL database
connection = mysql.connector.connect(user=username, password=password, host=host, database=database)

try:
    # Create a cursor to execute SQL queries
    cursor = connection.cursor()

    # Iterate over each table and corresponding CSV file
    for table, csv_path in csv_paths.items():
        with open(csv_path, newline='') as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                # Determine the table and construct the appropriate SQL query
                if table == "customers":
                    query = "INSERT INTO Customers (customer_id, customer_first_name, customer_last_name, customer_email, customer_address) VALUES (%s, %s, %s, %s, %s)"
                elif table == "orders":
                    query = "INSERT INTO Orders (order_id, cleaning_variant_fk, cleaning_duration, is_inside_cleaning, is_outside_cleaning, travel_distance, salesman_id_fk, customer_id_fk, cleaning_address, cleaning_date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                elif table == "workers":
                    query = "INSERT INTO Workers (worker_id, worker_first_name, worker_last_name, worker_email, worker_address) VALUES (%s, %s, %s, %s, %s)"
                elif table == "cleaningVariants":
                    query = "INSERT INTO Cleaning_Variants (variant_id, variant_name, variant_standard_cost_per_hour, variant_outside_cost_per_hour) VALUES (%s, %s, %s, %s)"
                
                # Execute the SQL query with the current row data
                cursor.execute(query, row)

    # Commit the transaction to save changes
    connection.commit()

except Exception as e:
    # Handle any exceptions that occur during the execution of the script
    print("An error occurred:", e)
    connection.rollback()

finally:
    # Close the cursor and connection to the database
    cursor.close()
    connection.close()