from flask import Flask
from blueprint.handlers import register_handler
from blueprint.student import student_blueprint
from blueprint.volunteer import volunteer_blueprint

app = Flask(__name__)

# Register error handler
register_handler(app)

# Register blueprints
app.register_blueprint(student_blueprint, url_prefix='/students')
app.register_blueprint(volunteer_blueprint, url_prefix='/volunteers')

if __name__ == '__main__':
    app.run(debug=True)