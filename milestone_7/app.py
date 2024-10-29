from flask import Flask, request, jsonify
import csv
from datetime import datetime

app = Flask(__name__)

def read_database (file_name):                              
    employees = []
    with open(file_name, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            employees.append(row) 
    return employees    

@app.get('/birthdays')
def get_birthdays ():

    month = request.args.get('month', '')
    department = request.args.get('department', '')

    if not month or not department:
        return jsonify({"error": "Відсутні необхідні параметри: місяць або департамент"}), 400
    
    db = read_database('database.csv')

    result = {'total': 0, 'employees': []}

    for emp in db:
        try:
            if not emp.get('birthday') or not emp.get('department'):
                continue
                
            emp_birthday = emp['birthday'].lower()
            emp_department = emp['department'].lower()
            
            if emp_birthday.startswith(month.lower()) and emp_department == department.lower():
                result["employees"].append({
                    "id": emp.get('id'),
                    "name": emp.get('name'),
                    "birthday": emp.get('birthday')
                })
                result["total"] += 1
        except Exception as e:
            print(f"Error processing employee: {str(e)}")
            continue
    
    if result["total"] == 0:
        return jsonify({"message": "Співробітників не знайдено"}), 404
        
    return jsonify(result) 
       


# @app.get('/database/anniversaries/< int: month>, <str: department>')
# def get_birthdays (month, department):
#     result = {}
#     for m, dept in file:
#         if m == month and dept == department:
#             return jsonify(result) 
#         elif m != month:
#             return 'Невірно введено місяць'
#         elif dept != department:
#             return 'Невірно введено департамент'
#         else:
#             'Невірно введено вхідні дані. Заповніть коректно місяць та департамент'


if __name__ == '__main__':
    app.run(debug=True, port=5000)