
from faker import Faker
import csv
from random import choice

fake = Faker()

def generate_base():
    departments = ['HR', 'Finance', 'Engineering', 'IT', 'Marketing']
    return {
        'id' : fake.pyint(min_value=1, max_value=10000),
        'full_name' : fake.name(),
        'birthday' : fake.date_of_birth(minimum_age=18, maximum_age=65),
        'department' : choice(departments),
        'phone' : fake.phone_number(),
        'emal' : fake.email(),
        'address' : fake.address(),
        'job' : fake.job(),
        'hiring_date' : fake.date_between(start_date = '-20y', end_date = 'today')
    }


database = [generate_base() for _ in range(100)]
print (database)

header = ['id', 'full_name', 'birthday', 'department', 'phone', 'emal', 'address', 'job', 'hiring_date']
with open('database.csv', 'w') as file:
    writer = csv.DictWriter(file, fieldnames=header)
    writer.writeheader()
    writer.writerows(database)

    