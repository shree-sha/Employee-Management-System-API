from flask import request, jsonify
from services.employee_service import (
    create_employee,
    get_all_employees
)

def add_employee():

    data = request.get_json(silent=True)

    if not data:
        return jsonify({
            "error": "JSON body required"
        }), 400

    employee = create_employee(data)

    return jsonify({
        "message": "Employee created",
        "employee": employee.to_dict()
    })

def get_employees():

    employees = get_all_employees()

    return jsonify([
        employee.to_dict()
        for employee in employees
    ])