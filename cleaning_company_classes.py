from faker import Faker
from itertools import count
import random
from datetime import datetime

class Person:
    def __init__(self):
        self.first_name = Faker().first_name()
        self.last_name = Faker().last_name()
        self.email = Faker().email()
        self.address = Faker().address()

class Salesman(Person):
    worker_count = count(start=1)

    def __init__(self):
        self.workerID = next(Salesman.worker_count)
        super().__init__()
        
class Customer(Person):
    customer_count = count(start=1)
    
    def __init__(self):
        self.customerID = next(Customer.customer_count)
        super().__init__()    
   
class CleaningVariant:
    variant_count = count(start = 100000, step = 100
                          )
    def __init__(self, variant_name, standard_cost_per_hour, cost_per_hour_with_outside):
        self.variantID = next(CleaningVariant.variant_count)
        self.variant_name = variant_name
        self.standard_cost_per_hour = standard_cost_per_hour
        self.cost_per_hour_with_outside = cost_per_hour_with_outside
 
fastCleaningVariant = CleaningVariant("Fast", 55, 90)
standardCleaningVariant = CleaningVariant("Standard", 75, 120)
silverCleaningVariant = CleaningVariant("Silver", 100, 150)
premiumCleaningVariant = CleaningVariant("Premium", 125, 180)
VIPCleaningVariant = CleaningVariant("VIP", 250, 400)

AllCleaningVariants = [
    fastCleaningVariant,
    standardCleaningVariant, 
    silverCleaningVariant, 
    premiumCleaningVariant, 
    VIPCleaningVariant
]

AllCleaningVariantsProbability = {
    fastCleaningVariant:        39, 
    standardCleaningVariant:    39, 
    silverCleaningVariant:      12, 
    premiumCleaningVariant:     8, 
    VIPCleaningVariant:         2
}

class Order:
    order_count = count(start=1)
    start_date = datetime(2024, 1, 1)
    end_date = datetime.now()
    
    def __init__(self, AllSalesmen, AllCustomers):
        self.orderID = next(Order.order_count)
        self.cleaning_variantID = random.choices(list(AllCleaningVariantsProbability.keys()), 
                                               AllCleaningVariantsProbability.values(), k=1)[0].variantID
        self.cleaning_duration = random.randint(1,12)
        self.is_inside_cleaning = random.choices([True, False], [0.96, 0.04], k=1)[0]
        self.is_outside_cleaning = random.choices([True, False], [0.22, 0.78], k=1)[0]
        self.travel_distance = random.randint(1,100)
        self.salesmanID = random.choice(AllSalesmen).workerID
        self.customerID = random.choice(AllCustomers).customerID
        self.cleaningAddress = Faker().address()
        self.cleaningDate = Faker().date_time_between_dates(Order.start_date, Order.end_date)
        
class CurrentOrder(Order):
    current_date = datetime.now().date()
    
    def __init__(self, SalesmenList, CustomersList):
        self.fakeSalesman = [Salesman()]
        self.fakeCustomer = [Customer()]
        super().__init__(self.fakeSalesman, self.fakeCustomer)
        self.salesmanID = random.choice(SalesmenList)
        self.customerID = random.choice(CustomersList)
        self.cleaningDate = CurrentOrder.current_date
        
        
