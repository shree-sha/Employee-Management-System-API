from flask import Blueprint

from controllers.employee_controller import (
    add_employee,
    get_employees,
    get_employee
)

employee_bp = Blueprint(
    "employee_bp",
    __name__
)

# Create Employee
employee_bp.route(
    "/employees",
    methods=["POST"]
)(add_employee)

# Get All Employees
employee_bp.route(
    "/employees",
    methods=["GET"]
)(get_employees)

# Get Employee By ID
employee_bp.route(
    "/employees/<int:employee_id>",
    methods=["GET"]
)(get_employee)