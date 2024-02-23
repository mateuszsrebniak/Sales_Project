from faker import Faker

class Worker:
    worker_count = 0  # Zmienna na poziomie klasy do śledzenia liczby pracowników

    def __init__(self):
        Worker.worker_count += 1
        self.workerID = Worker.worker_count
        self.first_name = Faker().first_name()
        self.last_name = Faker().last_name()
        self.email = Faker().email()
        self.address = Faker().address()
        
    def __str__(self):
        return f"Worker {self.workerID}: {self.first_name} {self.last_name}, Email: {self.email}"

class AllWorkers:
    def __init__(self, num_workers):
        self.workersList = [Worker() for _ in range(num_workers)]

    def __getitem__(self, index):
        return self.workersList[index]
    
    
# Ustaw ziarno dla całej klasy Faker
Faker.seed(0)

# Tworzenie obiektu Faker
fake = Faker()

for _ in range(5):
    # Ustaw ziarno dla konkretnego obiektu Faker
    fake.seed_instance(0)
    
    # Generuj daty i godziny pomiędzy podanym zakresem
    generated_datetime = fake.date_time_between(start_date="2024-01-01T08:00:00")
    
    # Wydrukuj wynik
    print(generated_datetime)