from faker import Faker
from itertools import count
import random

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
        
class Company:
    company_count = count(start=1)
    
    def __init__ (self):
        self.companyID = Company.company_count
        self.company_name = Faker().company()
        self.email = Faker().email()
        self.address = Faker().address()
        self.phone = Faker().phone()
        

class AllSalesmen:
    def __init__(self, num_workers):
        self.workersList = [Salesman() for _ in range(num_workers)]

    def __getitem__(self, index):
        return self.workersList[index]
    
class AllCustomers:
    def __init__(self, num_customers):
        self.customersList = [Customer() for _ in range(num_customers)]

    def __getitem__(self, index):
        return self.customersList[index]
    
class AllCompanies:
    def __init__(self, num_companies):
        self.companiesList = [Company() for _ in range(num_companies)]
    def __getitem__(self, index):
        return self.companiesList[index]
    
    
class CleaningVariant:
    def __init__(self, variant_name, standard_cost_per_hour, cost_per_hour_with_outside):
        self.variant_name = variant_name
        self.standard_cost_per_hour = standard_cost_per_hour
        self.cost_per_hour_with_outside = cost_per_hour_with_outside
 
fastCleaningVariant = CleaningVariant("Fast", 55, 90)
standardCleaningVariant = CleaningVariant("Standard", 75, 120)
silverCleaningVariant = CleaningVariant("Silver", 100, 150)
premiumCleaningVariant = CleaningVariant("Premium", 125, 180)
VIPCleaningVariant = CleaningVariant("VIP", 250, 400)

AllCleaningVariantsProbability = {
    fastCleaningVariant:39, 
    standardCleaningVariant:39, 
    silverCleaningVariant:12, 
    premiumCleaningVariant:8, 
    VIPCleaningVariant:2
}

class Order:
    order_count = count(start=1)
    
    def __init__(self, cleaning_variant: CleaningVariant,
                 cleaning_duration, is_inside_cleaning=True, is_outside_cleaning=False, travel_distance=0):
        self.OrderID = next(Order.order_count)
        self.cleaning_variant = random.choices(list(AllCleaningVariantsProbability.keys()), 
                                               AllCleaningVariantsProbability.values(), k=1)[0]
        self.cleaning_duration = random.randint(1,12)
        self.is_inside_cleaning = random.choices([True, False], [0.96, 0.04], k=1)[0]
        self.is_outside_cleaning = random.choices([True, False], [0.22, 0.78], k=1)[0]
        self.travel_distance = random.randint(1,100)
    
    