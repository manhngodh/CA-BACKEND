from app import db
from sqlalchemy.dialects.postgresql import JSON

class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    people_id = db.Column(db.String(255), unique=True, nullable=False)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    # ... other common attributes ...

class Student(People):
    __tablename__ = 'students'
    # ... student-specific attributes ...

class Volunteer(People):
    __tablename__ = 'volunteers'
    job_data = db.Column(JSON)
    # ... volunteer-specific attributes ...


class SchoolPerformance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    people_id = db.Column(db.String(255), db.ForeignKey('people.people_id'), nullable=False)
    school_performance = db.Column(JSON)
    person = db.relationship('People', backref=db.backref('school_performance_data', lazy=True))