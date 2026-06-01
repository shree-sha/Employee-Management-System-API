from flask import request, jsonify
from services.validation_service import validate_employee
from services.employee_service import (
    create_employee,
    get_all_employees,
    get_employee_by_id,
    update_employee,
    delete_employee,
    get_employees_by_department
)

def add_employee():

    data = request.get_json(silent=True)

    if not data:
        return jsonify({
            "error": "JSON body required"
        }), 400

    validation_error = validate_employee(data)

    if validation_error:
        return jsonify({
            "error": validation_error
        }), 400

    employee = create_employee(data)

    return jsonify({
        "message": "Employee created",
        "employee": employee.to_dict()
    })

from flask import request

def get_employees():

    department = request.args.get("department")

    page = request.args.get(
        "page",
        default=1,
        type=int
    )

    limit = request.args.get(
        "limit",
        default=5,
        type=int
    )

    employees = get_all_employees(
        department,
        page,
        limit
    )

    return [
        employee.to_dict()
        for employee in employees
    ], 200

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

    validation_error = validate_employee(data)

    if validation_error:
        return jsonify({
        "error": validation_error
    }), 400

    employee = update_employee(employee_id, data)

    return jsonify(
        employee.to_dict()
    )

def delete_employee_controller(employee_id):

    deleted = delete_employee(employee_id)

    if not deleted:
        return jsonify({
            "error": "Employee not found"
        }), 404

    return jsonify({
        "message": "Employee deleted successfully"
    })