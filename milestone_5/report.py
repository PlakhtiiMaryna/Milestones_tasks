import csv
import sys
from datetime import datetime
import argparse

def parse_date (string_date):
    return datetime.strptime(string_date, '%Y-%m-%d')      # перетворюємо місяць у формат дати

def month_number (month_name: str):                        # призначаємо кожному місяцю цифру
    months = {
       'january' : 1, 'february' : 2,  'march' : 3,
        'april' : 4, 'may' : 5, 'june' : 6,
        'july' : 7, 'august' : 8, 'september' : 9,
         'october' : 10, 'november' : 11, 'december' : 12 
    }
    return months.get(month_name.lower())

def read_database (file_name):                               # читаємо файл і дістаємо необхідні дані
    employees = []
    with open(file_name, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            employees.append({
                'name' : row['full_name'],
                'birthday' : parse_date(row['birthday']),
                'department' : row['department'],
                'hiring_date' : parse_date(row['hiring_date'])
            })
    return employees

def get_birthdays (employees, month, verbose = False):         # збираємо та рахуємо дані про дні народження і департаменти
    birthdays = {'total': 0, 'by_department' : {}}

    for emp in employees:
        if emp['birthday'].month == month:
            birthdays['total'] +=1
            dep = emp['department']
            if dep not in birthdays['by_department']:
                birthdays['by_department'][dep] = {'count' : 0, 'names' : []}
            birthdays['by_department'][dep]['count'] +=1
            if verbose:
                birthdays['by_department'][dep]['names'].append(emp['name'])
    return birthdays

def get_anniversaries (employees, month, verbose = False):                   # збираємо та рахуємо дані про робочі ювілеї і департаменти
    anniversaries = {'total' : 0, 'by_department' : {}}

    for emp in employees:
        if emp['hiring_date'].month == month:
            anniversaries['total'] +=1
            dep = emp['department']
            if dep not in anniversaries['by_department']:
                anniversaries['by_department'][dep] = {'count' : 0, 'names' : []}
            anniversaries['by_department'][dep]['count'] += 1
            if verbose:
                anniversaries['by_department'][dep]['names'].append(emp['name'])
    return anniversaries


def print_report(month_name, birthdays, anniversaries, verbose=False):
    print (f'Сформовано звіт за {month_name.capitalize()} місяць')                           # Виводимо звіт про дні народження
    print (f'Всього {birthdays["total"]} днів народження')
    print ('Дні народження у кожному відділі')
    for dep, data in birthdays['by_department'].items():
        print(f'- {dep} : {data["count"]}')
        if verbose and data['names']:
            for name in data['names']:
                print(f'-- {name}')


    print (f'Сформовано звіт за {month_name.capitalize()} місяць')                         # Виводимо звіт про робочі ювілеї
    print (f'Всього {anniversaries["total"]} робочих ювілеїв')
    print ('Ювілеї по кожному департаменту')
    for dep, data in anniversaries['by_department'].items():
        print(f'- {dep} : {data["count"]}')
        if verbose and data['names']:
            for name in data['names']:
                print(f'-- {name}')

def main():
    parser = argparse.ArgumentParser(description='Створити звіт про співробітників')
    parser.add_argument('database', help = 'Шлях до файлу бази даних')
    parser.add_argument('month', help = 'Місяць для створення звіту')
    parser.add_argument('-v', '--verbose', action='store_true', help= 'Включити імена співробітників у звіт')


    args = parser.parse_args()

    month_num = month_number(args.month)
    if not month_num:
        print(f'Помилка: Недійсна назва місяця {args.month}')
        sys.exit(1)

    try:
        employees = read_database(args.database)
        birthdays =  get_birthdays(employees, month_num, args.verbose)
        anniversaries = get_anniversaries(employees, month_num, args.verbose)
        print_report (args.month, birthdays, anniversaries, args.verbose)
    except FileNotFoundError:
        print(f'Помилка: Файл бази даних не знайдено {args.database}')
        sys.exit(1)
    except Exception as e:
        print(f'Помилка: {str(e)}')
        sys.exit(1)

if __name__ == '__main__':
    main()



    
