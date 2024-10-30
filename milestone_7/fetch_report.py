import requests
import sys
from datetime import datetime

if len(sys.argv) != 3:
    print ('Вкажіть три аргументи: python fetch_report.py <month> <department>')
    sys.exit(1)

month, department = sys.argv[1], sys.argv[2]

url = 'http://127.0.0.1:5000/birthdays'
params = {'month' : month, 'department' : department}

try:
    result = requests.get(url, params=params)
    result.raise_for_status

except requests.exceptions.RequestException as e:
    print (f'Помилка отримання звіту {e}')
    sys.exit(1)

data = result.json()

if 'error' in data:
    print (data ['error'])
elif 'message' in data:
    print (data ['message'])
else:
    print(f"Звіт для {department} департамент для {month.capitalize()} сформовано.")
    print(f"Всього: {data['total']}")
    print("Спвіробітники:")

for emp in data['employees']:
    emp_date = datetime.strptime(emp['birthday'], "%Y-%m-%d").strftime("%b %d")
    print (f'-{emp_date, emp['name']}')





