from flask import Blueprint
from controllers.employee_controller import (
    add_employee,
    get_employees
)

from controllers.employee_controller import add_employee

employee_bp = Blueprint(
    "employee_bp",
    __name__
)

employee_bp.route(
    "/employees",
    methods=["GET"]
)(get_employees)