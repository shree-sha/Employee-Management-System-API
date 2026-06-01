import re

def validate_employee(data):

    if not data.get("name"):
        return "Name is required"

    email = data.get("email")

    email_pattern = r"^[^@]+@[^@]+\.[^@]+$"

    if not email or not re.match(email_pattern, email):
        return "Invalid email"

    salary = data.get("salary")

    if salary is None or salary <= 0:
        return "Salary must be greater than 0"

    return None