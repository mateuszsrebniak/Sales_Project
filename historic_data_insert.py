import csv
import oracledb

# Ustawienia połączenia z bazą danych Oracle
username = "Cleaning_Company"
password = "cleaning"
dsn = "XEPDB1"

# Ścieżka do pliku CSV
csv_path_customers = "C:/Users/Mateusz/OneDrive/Pulpit/Nauka/Python/Sales_Project/historic_data/Customer.csv"
csv_path_orders = "C:/Users/Mateusz/OneDrive/Pulpit/Nauka/Python/Sales_Project/historic_data/Order.csv"
csv_path_workers = "C:/Users/Mateusz/OneDrive/Pulpit/Nauka/Python/Sales_Project/historic_data/Salesman.csv"
csv_path_cleaningVariants = "C:/Users/Mateusz/OneDrive/Pulpit/Nauka/Python/Sales_Project/historic_data/CleaningVariant.csv"

# Połączenie z bazą danych Oracle
connection = oracledb.connect(user=username, password=password, dsn=dsn)

# Utworzenie kursora
cursor = connection.cursor()

# Otwarcie pliku CSV
with open(csv_path_customers, newline='') as csv_file:
    csv_reader = csv.reader(csv_file)
    
    # Iteracja przez wiersze pliku CSV i wstawienie danych do bazy danych
    for row in csv_reader:
        # Zakładając, że kolumny w pliku CSV odpowiadają kolumnom w tabeli bazy danych
        query = "INSERT INTO customers (customer_first_name, customer_last_name, \
            customer_email, customer_address) VALUES (:1, :2, :3, :4)"
        cursor.execute(query, row[1:])
    
    # Zatwierdzenie transakcji
    connection.commit()

# Zamknięcie kursora i połączenia
cursor.close()

##############################################################

# Otwarcie pliku CSV
with open(csv_path_cleaningVariants, newline='') as csv_file:
    csv_reader = csv.reader(csv_file)
    
    # Iteracja przez wiersze pliku CSV i wstawienie danych do bazy danych
    for row in csv_reader:
        # Zakładając, że kolumny w pliku CSV odpowiadają kolumnom w tabeli bazy danych
        query = "INSERT INTO cleaning_variants (variant_id, variant_name, \
            variant_standard_cost_per_hour,variant_outside_cost_per_hour) \
                VALUES (:1, :2, :3, :4)"
        cursor.execute(query, row)
    
    # Zatwierdzenie transakcji
    connection.commit()

# Zamknięcie kursora i połączenia
cursor.close()

##############################################################

# Otwarcie pliku CSV
with open(csv_path_workers, newline='') as csv_file:
    csv_reader = csv.reader(csv_file)
    
    # Iteracja przez wiersze pliku CSV i wstawienie danych do bazy danych
    for row in csv_reader:
        # Zakładając, że kolumny w pliku CSV odpowiadają kolumnom w tabeli bazy danych
        query = "INSERT INTO workers (worker_first_name, worker_last_name, \
#             worker_email, worker_address) VALUES (:1, :2, :3, :4)"
        cursor.execute(query, row[1:])
    
    # Zatwierdzenie transakcji
    connection.commit()

# Zamknięcie kursora i połączenia
cursor.close()

##############################################################

# Otwarcie pliku CSV
with open(csv_path_orders, newline='') as csv_file:
    csv_reader = csv.reader(csv_file)
    
    # Iteracja przez wiersze pliku CSV i wstawienie danych do bazy danych
    for row in csv_reader:
        print(row)
        # Zakładając, że kolumny w pliku CSV odpowiadają kolumnom w tabeli bazy danych
        query = "INSERT INTO orders (cleaning_variant_fk, cleaning_duration, is_inside_cleaning, \
                                    is_outside_cleaning, travel_distance, salesman_id_fk, customer_id_fk, \
                                    cleaning_address, cleaning_date) \
                                    VALUES (:1, :2, :3, :4, :5, :6, :7, :8, :9)"
        cursor.execute(query, row[1:])
    
    # Zatwierdzenie transakcji
    connection.commit()

# Zamknięcie kursora i połączenia
cursor.close()
connection.close()

##############################################################