from flask import Blueprint, request, jsonify
from app.blueprints.api_utils import decrypt_people_id

student_blueprint = Blueprint('student', __name__)

# Example storage for student scores
student_scores = {}

@student_blueprint.route('/<encrypted_people_id>/advices', methods=['POST'])
def get_advice(encrypted_people_id):
    decrypted_people_id = decrypt_people_id(encrypted_people_id)
    data = request.json
    
    # Extract subject scores from the request data
    math_score = data.get("math_score")
    physics_score = data.get("physics_score")
    chemistry_score = data.get("chemistry_score")
    biology_score = data.get("biology_score")
    literature_score = data.get("literature_score")
    history_score = data.get("history_score")
    geography_score = data.get("geography_score")
    philosophy_score = data.get("philosophy_score")
    art_score = data.get("art_score")
    foreign_language_score = data.get("foreign_language_score")
    
    # Store student scores
    student_scores[decrypted_people_id] = {
        "math": math_score,
        "physics": physics_score,
        "chemistry": chemistry_score,
        "biology": biology_score,
        "literature": literature_score,
        "history": history_score,
        "geography": geography_score,
        "philosophy": philosophy_score,
        "art": art_score,
        "foreign_language": foreign_language_score
    }
    
    # Calculate recommendation logic based on scores and job earnings data
    # Implement your recommendation logic here
    
    # For example, returning dummy recommendations
    recommended_jobs = [
        {"job_name": "Software Engineer", "average_earnings": 100000},
        {"job_name": "Data Scientist", "average_earnings": 95000}
    ]
    
    return jsonify({"recommended_jobs": recommended_jobs})
