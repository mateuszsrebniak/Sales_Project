import csv
import os
from cleaning_company_classes import Salesman, Order, Customer, AllCleaningVariants

def dump_data_to_csv(data_object, folder_to_store_file_path):
    
    # Sprawdzenie, czy folder istnieje; jeśli nie, utwórz go
    if not os.path.exists(folder_to_store_file_path):
        os.makedirs(folder_to_store_file_path)

    csv_file_name = os.path.join(folder_to_store_file_path, f"{data_object[0].__class__.__name__}.csv")

    fieldnames = list(data_object[0].__dict__.keys())

    with open(csv_file_name, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        for obj in data_object:
            writer.writerow(obj.__dict__)

AllSalesmen = [Salesman() for _ in range(62)]
AllCustomers = [Customer() for _ in range(1088)]
AllOrders = [Order(AllSalesmen, AllCustomers) for _ in range(11091)]

AllData = [AllSalesmen, AllCustomers, AllOrders, AllCleaningVariants]

my_folder_path = "C:/Users/Mateusz/OneDrive/Pulpit/Nauka/Python/Sales_Project/historic_data"

for obj in AllData:
    try:
        dump_data_to_csv(obj, my_folder_path)
    except Exception as e:
        print(f"Error: {e}")
