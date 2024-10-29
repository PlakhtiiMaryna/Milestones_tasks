from flask import Flask, request, jsonify
import csv

app = Flask(__name__)

def read_database (file_name):                              
    employees = []
    with open(file_name, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            employees.append(row) 
    return employees    

@app.get('/database/birthdays/< int: month>, <str: department>')
def get_birthdays (month, department):
    result = {}
    for m, dept in file:
        if m == month and dept == department:
            return jsonify(result) 
        elif m != month:
            return 'Невірно введено місяць'
        elif dept != department:
            return 'Невірно введено департамент'
        else:
            'Невірно введено вхідні дані. Заповніть коректно місяць та департамент'


@app.get('/database/anniversaries/< int: month>, <str: department>')
def get_birthdays (month, department):
    result = {}
    for m, dept in file:
        if m == month and dept == department:
            return jsonify(result) 
        elif m != month:
            return 'Невірно введено місяць'
        elif dept != department:
            return 'Невірно введено департамент'
        else:
            'Невірно введено вхідні дані. Заповніть коректно місяць та департамент'


if __name__ == '__main__':
    app.run()