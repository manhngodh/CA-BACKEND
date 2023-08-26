from app.database import db
from sqlalchemy.dialects.postgresql import JSON
from app.schemas import JobDataSchema
from dataclasses import dataclass

class People(db.Model):
    __tablename__ = 'people'
    id = db.Column(db.Integer, primary_key=True)
    people_id = db.Column(db.String, nullable=False, unique=True)
    role = db.Column(db.Integer, nullable=False)  # 1 for Student, 2 for Volunteer
    school_performance = db.relationship('SchoolPerformance', backref='people', uselist=False, lazy=True)
    def school_performance_data(people_id):
        return SchoolPerformance.query.filter(People.people_id==people_id).first()

@dataclass
class SchoolPerformance(db.Model):
    __tablename__ = 'school_performance'
    id = db.Column(db.Integer, primary_key=True)
    people_id = db.Column(db.String, db.ForeignKey('people.people_id'), nullable=False, unique=True)
    math = db.Column(db.Float, nullable=False)
    physics = db.Column(db.Float, nullable=False)
    chemistry = db.Column(db.Float, nullable=False)
    biology = db.Column(db.Float, nullable=False)
    literature = db.Column(db.Float, nullable=False)
    history = db.Column(db.Float, nullable=False)
    geography = db.Column(db.Float, nullable=False)
    philosophy = db.Column(db.Float, nullable=False)
    art = db.Column(db.Float, nullable=False)
    foreign_language = db.Column(db.Float, nullable=False)

    def __init__(self, people_id, scores):
        self.people_id = people_id
        self.math = scores.get('math', self.math)
        self.physics = scores.get('physics', self.physics)
        self.chemistry = scores.get('chemistry', self.chemistry)
        self.biology = scores.get('biology', self.biology)
        self.literature = scores.get('literature', self.literature)
        self.history = scores.get('history', self.history)
        self.geography = scores.get('geography', self.geography)
        self.philosophy = scores.get('philosophy', self.philosophy)
        self.art = scores.get('art', self.art)
        self.foreign_language = scores.get('foreign_language', self.foreign_language)
    
    def update_scores(self, updated_scores):
        self.math = updated_scores.get('math', self.math)
        self.physics = updated_scores.get('physics', self.physics)
        self.chemistry = updated_scores.get('chemistry', self.chemistry)
        self.biology = updated_scores.get('biology', self.biology)
        self.literature = updated_scores.get('literature', self.literature)
        self.history = updated_scores.get('history', self.history)
        self.geography = updated_scores.get('geography', self.geography)
        self.philosophy = updated_scores.get('philosophy', self.philosophy)
        self.art = updated_scores.get('art', self.art)
        self.foreign_language = updated_scores.get('foreign_language', self.foreign_language)

    def to_json(self):
        return self.__dict__


class JobData(db.Model):
    __tablename__ = 'job_data'
    id = db.Column(db.Integer, primary_key=True)
    people_id = db.Column(db.String, db.ForeignKey('people.people_id'), nullable=False)
    job_title = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=True)
    skills = db.Column(db.JSON, nullable=True)

    def __init__(self,people_id, job):
        self.people_id = people_id
        self.job_title = job.get('job_title', self.job_title)
        self.description = job.get('description', self.description)
        self.skills = job.get('skills', self.skills)
        
    def update(self, job):
        self.job_title = job.get('job_title', self.job_title)
        self.description = job.get('description', self.description)
        self.skills = job.get('skills', self.skills)

    # ... other methods and properties ...

    def serialize(self):
        schema = JobDataSchema()
        return schema.dump(self)