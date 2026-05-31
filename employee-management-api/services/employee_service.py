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

def get_all_employees():
    return Employee.query.all()