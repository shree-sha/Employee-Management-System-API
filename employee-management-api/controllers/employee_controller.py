from flask import request, jsonify

from services.employee_service import create_employee

def add_employee():

    data = request.json

    employee = create_employee(data)

    return jsonify({
        "message": "Employee created",
        "employee": employee.to_dict()
    })