from flask import Blueprint, request, jsonify
from app.blueprint.utils import decrypt_people_id

volunteer_blueprint = Blueprint('volunteer', __name__, url_prefix='/volunteers')

# Example storage for volunteer jobs
volunteer_jobs = {}

@volunteer_blueprint.route('/<people_id>/jobs', methods=['POST'])
@app.route('/<string:people_id>/jobs', methods=['POST'])
def add_jobs(people_id):
    # Check if school performance data exists for the volunteer
    if not has_school_performance(people_id):
        return error_response("School performance data required before adding job information")

    # Retrieve the volunteer from the database
    volunteer = Volunteer.query.filter_by(people_id=people_id).first()
    if not volunteer:
        return error_response("Volunteer not found", status_code=404)

    # Parse job data from the request
    job_data = request.json.get('jobs', [])

    # Validate job data
    if not isinstance(job_data, list):
        return error_response("Invalid job data format", status_code=400)

    # Save job data to the database
    try:
        for job_name in job_data:
            job = Job(volunteer_id=volunteer.id, job_name=job_name)
            db.session.add(job)

        db.session.commit()
        return success_response(message="Job information added successfully")
    except Exception as e:
        db.session.rollback()
        return error_response("Error adding job information", status_code=500)
    finally:
        db.session.close()

@volunteer_blueprint.route('/<encrypted_people_id>/jobs', methods=['GET'])
def get_jobs(encrypted_people_id):
    decrypted_people_id = decrypt_people_id(encrypted_people_id)
    
    # Retrieve volunteer jobs from storage
    jobs = volunteer_jobs.get(decrypted_people_id, [])
    
    return jsonify({"jobs": jobs})

# Implement other endpoints for updating and deleting jobs


"""
{
  "jobs": [
    {
      "title": "Software Engineer",
      "company": "ABC Tech",
      "salary": 100000
    },
    {
      "title": "Data Analyst",
      "company": "XYZ Analytics",
      "salary": 80000
    }
  ]
}
"""