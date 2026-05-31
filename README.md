# Employee Management API

A RESTful API built using Python and Flask for managing employee records.

## Features

* Create Employee
* View Employees
* Update Employee
* Delete Employee

## Tech Stack

* Python
* Flask
* SQLAlchemy
* SQLite
* Git
* Postman

## Setup

1. Clone repository
2. Create virtual environment
inside a folder employee-managemnet-api
-> python -m venv venv #creating virutal environment
-> venv\scripts\activate #activating virtual environment
3. Install requirements
-> pip install flask flask-sqlalchemy
-> pip freeze > requirements.txt #save requirements(optinal)
4. Run application

## Project Architecture

employee-management-api

config/
models/
controllers/
services/
routes/

### Flow

Request
→ Route
→ Controller
→ Service
→ Model
→ Database

## Completed Features

* Flask project setup
* MVC architecture
* SQLite database integration
* SQLAlchemy ORM
* Employee model
* Create Employee API (POST /employees)

## API Example

### Create Employee

POST /employees

Request:

{
"name": "John",
"email": "[john@gmail.com](mailto:john@gmail.com)",
"department": "Engineering",
"salary": 50000
}

Response:

{
"message": "Employee created",
"employee": {
"id": 1,
"name": "John",
"email": "[john@gmail.com](mailto:john@gmail.com)",
"department": "Engineering",
"salary": 50000
}
}

## Endpoints

POST /employees
GET /employees
GET /employees/<id>