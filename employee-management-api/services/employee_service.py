# Business logic goes here

from models.employee import Employee
from config.database import db


def create_employee(data):

    employee = Employee(
        name=data["name"],
        email=data["email"],
        department=data["department"],
        salary=data["salary"]
    )

    db.session.add(employee)
    db.session.commit()

    return employee

from models.employee import Employee

def get_all_employees(department=None):

    if department:
        return Employee.query.filter_by(
            department=department
        ).all()

    return Employee.query.all()

def get_employee_by_id(employee_id):
    return Employee.query.get(employee_id)

def update_employee(employee_id, data):

    employee = Employee.query.get(employee_id)

    if not employee:
        return None

    employee.name = data["name"]
    employee.email = data["email"]
    employee.department = data["department"]
    employee.salary = data["salary"]

    db.session.commit()

    return employee

def delete_employee(employee_id):

    employee = Employee.query.get(employee_id)

    if not employee:
        return False

    db.session.delete(employee)
    db.session.commit()

    return True

def get_employees_by_department(department):

    return Employee.query.filter_by(
        department=department
    ).all()