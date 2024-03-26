import oracledb
from random import randint
from cleaning_company_classes import Order


 
# TodaysOrders = [Order(AllSalesmen, AllCustomers) for _ in range(1)]


with oracledb.connect(user="CLEANING_COMPANY", password="cleaning",
                              dsn="XEPDB1", 
                              config_dir="C:/app/Mateusz/product/21c/dbhomeXE/network/admin"
                              ) as connection:

    cur = connection.cursor()
    cur.execute('SELECT worker_id FROM WORKERS')
    AllSalesmen = cur.fetchall()    
    cur.close()
    
print(results)