from flask import request, jsonify
from services.employee_service import (
    create_employee,
    get_all_employees,
    get_employee_by_id,
    update_employee
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

def get_employee(employee_id):

    employee = get_employee_by_id(employee_id)

    if not employee:
        return jsonify({
            "error": "Employee not found"
        }), 404

    return jsonify(
        employee.to_dict()
    )

def update_employee_controller(employee_id):

    data = request.get_json(silent=True)

    if not data:
        return jsonify({
            "error": "JSON body required"
        }), 400

    employee = update_employee(employee_id, data)

    if not employee:
        return jsonify({
            "error": "Employee not found"
        }), 404

    return jsonify(
        employee.to_dict()
    )