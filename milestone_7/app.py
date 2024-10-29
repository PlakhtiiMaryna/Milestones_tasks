from flask import Flask, request, jsonify
import csv
from datetime import datetime

app = Flask(__name__)

MONTHS = {
    "січень": "01", "january": "01", "лютий": "02", "february": "02",
    "березень": "03", "march": "03", "квітень": "04", "april": "04",
    "травень": "05", "may": "05", "червень": "06", "june": "06",
    "липень": "07", "july": "07", "серпень": "08", "august": "08",
    "вересень": "09", "september": "09", "жовтень": "10", "october": "10",
    "листопад": "11", "november": "11", "грудень": "12", "december": "12"
}

def read_database(file_name):                              
    employees = []
    with open(file_name, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            employees.append(row) 
    return employees    

def normalize_month(month):
    month = month.lower().strip()
    return MONTHS.get(month, f"{int(month):02d}" if month.isdigit() and 1 <= int(month) <= 12 else None)

@app.get('/birthdays')
def get_birthdays():
    month = request.args.get('month', '')
    department = request.args.get('department', '')

    if not month or not department:
        return jsonify({"Помилка": "Відсутні необхідні параметри: місяць або департамент"}), 400
    
    db = read_database('database.csv')
    result = {'total': 0, 'employees': []}

    normalized_month = normalize_month(month)
    if not normalized_month:
        return jsonify({"Помилка": "Неправильний формат місяця"}), 400

    for emp in db:
        try:
            if not emp.get('birthday') or not emp.get('department'):
                continue
                
            emp_birthday = emp['birthday']
            emp_department = emp['department'].lower()

            emp_month = datetime.strptime(emp_birthday, '%Y-%m-%d').strftime('%m')
            
            if emp_month == normalized_month and emp_department == department.lower():
                result["employees"].append({
                    "id": emp.get('id'),
                    "name": emp.get('full_name'),  
                    "birthday": emp.get('birthday')
                })
                result["total"] += 1
        except Exception as e:
            app.logger.error(f"Помилка обробки співробітника: {str(e)}")
            continue

    if result["total"] == 0:
        return jsonify({"Повдомлення" : "Співробітників не знайдено"}), 404
        
    return jsonify(result)

@app.get('/anniversaries')
def get_anniversaries():
    month = request.args.get('month', '')
    department = request.args.get('department', '')

    if not month or not department:
        return jsonify({"Помилка": "Відсутні необхідні параметри: місяць або департамент"}), 400
    
    db = read_database('database.csv')
    result = {'total' : 0, 'employees' : []}

    normalized_month = normalize_month(month)
    if not normalized_month:
        return jsonify({"Помилка": "Неправильний формат місяця"}), 400
    
    for emp in db:
        try:
            if not emp.get('hiring_date') or not emp.get('department'):
                continue

            emp_hiring_date = emp['hiring_date']
            emp_department = emp['department'].lower()

            emp_month = datetime.strptime(emp_hiring_date, '%Y-%m-%d').strftime('%m')

            if emp_month == normalized_month and emp_department == department.lower():
                result["employees"].append({
                    'id' : emp.get('id'),
                    'name' : emp.get('full_name'),
                    'hiring_date' : emp.get('hiring_date')
                })
                result["total"] += 1
        
        except Exception as e:
            app.logger.error(f"Помилка обробки співробітника: {str(e)}")
            continue

    if result['total'] == 0:
        return jsonify({"Повдомлення" : "Співробітників не знайдено"}), 404
    
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True, port=5000)