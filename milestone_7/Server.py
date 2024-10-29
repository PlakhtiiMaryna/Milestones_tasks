from flask import Flask, request, jsonify
import csv

app = Flask(__name__)

def read_database(file_name):
    employees = []
    with open(file_name, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            employees.append(row)
    return employees

@app.get('/birthdays')
def get_birthdays():
    month = request.args.get('month')
    department = request.args.get('department')
    DB = read_database('database.csv')
    result = {'total': 0, 'employees': []}
    
    for emp in DB:
        if emp['birthday'] and emp['department']:
            if emp['birthday'].lower().startswith(month.lower()) and emp['department'].lower() == department.lower():
                result["employees"].append({
                    "id": emp['id'],
                    "name": emp['name'],
                    "birthday": emp['birthday']
                })
                result['total'] += 1  # Increment total count

    if result['total'] == 0:
        return jsonify({'message': 'Співробітників не знайдено'}), 404  # Return JSON response

    return jsonify(result)

@app.get('/anniversaries')
def get_anniversaries():
    month = request.args.get('month')
    department = request.args.get('department')
    DB = read_database('database.csv')
    result = {'total': 0, 'employees': []}
    
    for emp in DB:
        if emp['anniversary'] and emp['department']:
            if emp['anniversary'].lower().startswith(month.lower()) and emp['department'].lower() == department.lower():
                result["employees"].append({
                    "id": emp['id'],
                    "name": emp['name'],
                    "anniversary": emp['anniversary']
                })
                result['total'] += 1  # Increment total count

    if result['total'] == 0:
        return jsonify({'message': 'Співробітників не знайдено'}), 404  # Return JSON response

    return jsonify(result)

if __name__ == '__main__':
    app.run(port=5000)