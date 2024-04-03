import oracledb
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
username = "Cleaning_Company"
password = "cleaning"
dsn = "XEPDB1"

# Połączenie z bazą danych Oracle
connection = oracledb.connect(user=username, password=password, dsn=dsn)

# Pobranie identyfikatorów pracowników (salesmen)
allSalesmen = fetch_ids_from_table("workers", "worker_id", connection)

# Pobranie identyfikatorów klientów (customers)
allCustomers = fetch_ids_from_table("customers", "customer_id", connection)

newOrdersCount = randint(60,180)

newOrders = [CurrentOrder(allSalesmen, allCustomers) for _ in range(1)]

cursor = connection.cursor()

for order in newOrders:
    query = f"INSERT INTO orders (cleaning_variant_fk, cleaning_duration, is_inside_cleaning, \
                                    is_outside_cleaning, travel_distance, salesman_id_fk, customer_id_fk, \
                                    cleaning_address, realization_date) \
                                    VALUES (:1, :2, :3, :4, :5, :6, :7, :8, TO_DATE(:9, 'YYYY-MM-DD'))"
    cursor.execute(query, (order.cleaning_variantID, order.cleaning_duration, order.is_inside_cleaning,
                            order.is_outside_cleaning, order.travel_distance, order.salesmanID,
                            order.customerID, order.cleaningAddress, order.cleaningDate))
    
    
connection.commit()
cursor.close()
connection.close()