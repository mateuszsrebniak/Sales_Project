import sys
sys.path.append("c:\\Users\\Mateusz\\OneDrive\\Pulpit\\Nauka\\Python\\Sales_Project\\.venv\\Lib\\site-packages")
import mysql.connector
from random import randint
from cleaning_company_classes import CurrentOrder

def fetch_ids_from_table(table_name, column_name, connection):
    cursor = connection.cursor()
    ids = []
    query = f"SELECT {column_name} FROM {table_name}"
    cursor.execute(query)
    for row in cursor:
        ids.append(row[0])
    cursor.close()
    return ids

# Ustawienia połączenia z bazą danych Oracle
username = "root"
password = "admin"
host = "localhost"
database = "Cleaning_Company"

# Establish a connection to the MySQL database
connection = mysql.connector.connect(user=username, password=password, host=host, database=database)

# Pobranie identyfikatorów pracowników (salesmen)
allSalesmen = fetch_ids_from_table("workers", "worker_id", connection)

# Pobranie identyfikatorów klientów (customers)
allCustomers = fetch_ids_from_table("customers", "customer_id", connection)

try:
    # Create a cursor to execute SQL queries
    cursor = connection.cursor()
    
    newOrdersCount = randint(60,180)
    newOrders = (CurrentOrder(allSalesmen, allCustomers) for _ in range(newOrdersCount))
    
    for order in newOrders:
        query = f"INSERT INTO orders (cleaning_variant_fk, cleaning_duration, is_inside_cleaning, \
                                        is_outside_cleaning, travel_distance, salesman_id_fk, customer_id_fk, \
                                        cleaning_address, cleaning_date) \
                                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(query, (order.cleaning_variantID, order.cleaning_duration, order.is_inside_cleaning,
                                order.is_outside_cleaning, order.travel_distance, order.salesmanID,
                                order.customerID, order.cleaningAddress, order.cleaningDate))

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