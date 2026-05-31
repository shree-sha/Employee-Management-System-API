from flask import request, jsonify
from services.employee_service import create_employee

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