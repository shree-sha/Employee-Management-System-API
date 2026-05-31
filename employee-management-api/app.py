from flask import Flask

from config.database import db
from routes.employee_routes import employee_bp

app = Flask(__name__)

app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "sqlite:///database/employees.db"

db.init_app(app)

app.register_blueprint(employee_bp)

@app.route("/")
def home():
    return {
        "message": "Employee API Running"
    }

if __name__ == "__main__":

    with app.app_context():
        db.create_all()

    app.run(debug=True)