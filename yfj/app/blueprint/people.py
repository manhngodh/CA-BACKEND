from flask import Blueprint, request, jsonify
from app.database import db
from app.models import People, SchoolPerformance
import requests
from app.blueprint.utils import encrypt_people_id
from app.blueprint.constants import Role

people_bp = Blueprint('people', __name__, url_prefix='/people')

@people_bp.route('/<string:people_id>/school_performance', methods=['POST', 'DELETE', 'PUT'])
def school_performance(people_id):

    try:
        encrypted_people_id = encrypt_people_id(people_id)
        people = People.query.filter(People.people_id==encrypted_people_id).first()
        if not people:
            return jsonify({'message': 'People not found'}), 404
        school_performance = people.school_performance

        # for creating 
        if request.method == 'POST':
            if school_performance:
                return jsonify(message="Already had school performance"), 400 
            data = request.json
            scores = data.get('school_performance')
            if scores is None or not isinstance(scores, dict):
                return jsonify(message="Invalid school performance data"), 400 

            #  Create or update school performance data in the database
            new_school_performance = SchoolPerformance(people_id=encrypted_people_id, scores=scores)
            db.session.add(new_school_performance)
            db.session.commit()
            return jsonify(message="School performance data added successfully"), 201

        # for updating
        if request.method == 'PUT':
            data = request.json
            scores = data.get('school_performance')
            if scores is None or not isinstance(scores, dict):
                return jsonify(message="Invalid school performance data"), 400 

            if not school_performance:
                return jsonify({'message': 'School performance data not found'}), 404
        
            # Update the school performance data
            school_performance.update_scores(scores)
            db.session.commit()
            return jsonify({'message': 'School performance updated successfully'}), 200

        # for deleting
        if request.method == 'DELETE':
            if school_performance:
                db.session.delete(school_performance)
                db.session.commit()
                return jsonify(message="School performance data deleted successfully")
            return jsonify(message="School performance data not found"), 404
    except Exception as e:
        return jsonify(error=str(e)), 500

"""
    CREATE
    curl --location 'http://localhost:9000/people/duc-nx/school_performance' \
    --header 'Content-Type: application/json' \
    --data '{
        "school_performance":{
            "math": 90,
            "physics": 85,
            "chemistry": 78,
            "biology": 92,
            "literature": 88,
            "history": 76,
            "geography": 82,
            "philosophy": 95,
            "art": 80,
            "foreign_language": 92
        }
    }'

    UPDATE
    curl --location --request PUT 'http://localhost:9000/people/duc-nx/school_performance' \
    --header 'Content-Type: application/json' \
    --data '{
        "school_performance":{
            "math": 90,
            "physics": 85,
            "chemistry": 78,
            "biology": 92,
            "literature": 88,
            "history": 76,
            "geography": 82,
            "philosophy": 95,
            "art": 80,
            "foreign_language": 92
        }
    }'
"""
@people_bp.route('/', methods=['GET'])
def test():
    return "Success"
