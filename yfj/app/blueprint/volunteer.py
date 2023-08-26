from flask import Blueprint, request, jsonify
from app.blueprint.utils import encrypt_people_id
from app.models import People, JobData, SchoolPerformance
from app.blueprint.constants import Role
from app.schemas import ListJobDataSchema
from app.database import db
from flask import current_app as app

volunteer_bp = Blueprint('volunteer', __name__, url_prefix='/volunteer')

@volunteer_bp.route('/<string:people_id>/jobs', methods=['POST'])
def add_job(people_id):
    """
      curl --location 'http://localhost:9000/volunteer/duc-nx/jobs' \
      --header 'Content-Type: application/json' \
      --data '{
          "jobs": [
              {
                  "job_title": "Sport and exercise psychologist",
                  "description": "This job involves helping individuals improve their performance, cope with stress, and maintain mental health.",
                  "skills": ["Psychology", "Physical fitness", "Communication"]
              },
              {
                  "job_title": "IT technical support officer",
                  "description": "Responsible for troubleshooting technical issues, installing and configuring software, and providing technical assistance to clients.",
                  "skills": ["IT support", "Troubleshooting", "Communication"]
              },
              {
                  "job_title": "Multimedia programmer",
                  "description": "Involves creating interactive multimedia products, combining various media elements such as text, graphics, audio, and video.",
                  "skills": ["Programming", "Multimedia design", "Creativity"]
              }
          ]
      }'
    """
    try:
        encrypted_people_id = encrypt_people_id(people_id)
        volunteer = People.query.filter(People.people_id==encrypted_people_id).filter(People.role==Role.Volunteer).first()
        if not volunteer:
            return jsonify(message="Volunteer not found"), 404
        
        # Check if the volunteer has school performance data
        school_performance = volunteer.school_performance
        if not school_performance:
            return jsonify(message="Please input school performance before adding job data"), 400

        data = request.json
        list_job_schema = ListJobDataSchema()
        # Load and validate the input data using the schema
        validated_data = list_job_schema.load(data)

        # Save job data to the database
        job_data_list = []
        for job in validated_data["jobs"]:
            job_data = JobData(people_id=encrypted_people_id, job=job)
            job_data_list.append(job_data)
            db.session.add(job_data)
        db.session.commit()
        return jsonify(message="Job data added successfully")

    except ValidationError as error:
        return jsonify(message="Invalid job data"), 400
    except Exception as e:
        app.logger.exception(e)
        return jsonify(error=str(e)), 500
    finally:
        db.session.close()

