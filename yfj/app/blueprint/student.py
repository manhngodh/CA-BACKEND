from flask import Blueprint, request, jsonify
from app.database import db
from app.models import People, SchoolPerformance
import requests
from app.blueprint.utils import encrypt_people_id
from app.blueprint.constants import Role
from app.score_computation import recommend_jobs


student_bp = Blueprint('student', __name__, url_prefix='/student')

@student_bp.route('/<string:people_id>/advices', methods=['GET'])
def student_advices(people_id):
    # Expect output
    """
        curl --location 'http://localhost:9000/student/manh-nx/advices'

        Expected output:
        {
            "recommended_jobs": [
                {
                    "compatibility_score": 112.0,
                    "job_title": "Pharmacologist",
                    "salary": 37000
                },
                {
                    "compatibility_score": 106.4,
                    "job_title": "Neurosurgeon",
                    "salary": 76000
                },
                {
                    "compatibility_score": 105.19999999999999,
                    "job_title": "Clinical biochemist",
                    "salary": 73000
                }
            ]
        }
    """
    try:
        encrypted_people_id = encrypt_people_id(people_id)
        student:People = People.query.filter(People.people_id==encrypted_people_id, People.role==Role.Student).first()
        if not student:
            return jsonify({'message': 'Student not found'}), 404
        
        school_performance = student.school_performance
        if not school_performance:
            return jsonify({'message': 'School performance data missing'}), 400

        school_performance = school_performance.to_json()
        recommended_jobs = recommend_jobs(school_performance)

        return jsonify({'recommended_jobs': recommended_jobs}), 200
    except Exception as error:
        return jsonify(error=str(error)), 500 


