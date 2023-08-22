from flask import Blueprint, request, jsonify
from app.blueprints.api_utils import decrypt_people_id

volunteer_blueprint = Blueprint('volunteer', __name__)

# Example storage for volunteer jobs
volunteer_jobs = {}

@volunteer_blueprint.route('/<encrypted_people_id>/jobs', methods=['POST'])
def add_jobs(encrypted_people_id):
    decrypted_people_id = decrypt_people_id(encrypted_people_id)
    data = request.json
    
    # Extract job names from the request data
    jobs = data.get("jobs", [])
    
    # Store volunteer jobs
    volunteer_jobs[decrypted_people_id] = jobs
    
    return jsonify({"message": "Jobs added successfully"})

@volunteer_blueprint.route('/<encrypted_people_id>/jobs', methods=['GET'])
def get_jobs(encrypted_people_id):
    decrypted_people_id = decrypt_people_id(encrypted_people_id)
    
    # Retrieve volunteer jobs from storage
    jobs = volunteer_jobs.get(decrypted_people_id, [])
    
    return jsonify({"jobs": jobs})

# Implement other endpoints for updating and deleting jobs
