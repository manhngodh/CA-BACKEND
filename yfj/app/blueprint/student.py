from flask import Blueprint, request, jsonify
from app.database import db
from app.models import Student
import requests

student_blueprint = Blueprint('student', __name__, url_prefix='/students')

# Function to fetch job earnings data from the service
def fetch_job_earnings():
    try:
        response = requests.get("http://localhost:8000/job_earnings")
        if response.status_code == 200:
            return response.json()
        return None
    except Exception as e:
        # app.logger.error(f"Error fetching job earnings: {e}")
        return None

@student_blueprint.route('/<encrypted_people_id>/advices', methods=['POST'])
def get_advice(encrypted_people_id):
    data = request.json
    student = Student.query.filter_by(encrypted_people_id=encrypted_people_id).first()

    if not student:
        student = Student(encrypted_people_id=encrypted_people_id)

    student.update_scores(data)
    db.session.add(student)
    db.session.commit()

    # Fetch job earnings data from the service
    job_earnings_data = fetch_job_earnings()

    if job_earnings_data:
        # Combine job earnings data with student scores to improve recommendation
        # Implement your recommendation logic here using job earnings data and student scores
        # ...
        # For example, returning dummy recommendations
        recommended_jobs = [
            {"job_name": "Software Engineer", "average_earnings": 100000},
            {"job_name": "Data Scientist", "average_earnings": 95000}
        ]
    else:
        # Fallback recommendation logic without job earnings data
        # ...
        recommended_jobs = [
            {"job_name": "Undetermined Job", "average_earnings": 0}
        ]

    return jsonify({"recommended_jobs": recommended_jobs})

@student_blueprint.route('/', methods=['GET'])
def test():
    return "Success"
