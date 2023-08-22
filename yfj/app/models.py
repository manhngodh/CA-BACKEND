from sqlalchemy import Column, Integer, String, Boolean, DateTime
from app.database import db


class Test(db.Model):
    __tablename__ = 'test'
    id = Column(Integer, primary_key=True)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    encrypted_people_id = db.Column(db.String(255), unique=True)
    math_score = db.Column(db.Float)
    physics_score = db.Column(db.Float)
    chemistry_score = db.Column(db.Float)
    biology_score = db.Column(db.Float)
    literature_score = db.Column(db.Float)
    history_score = db.Column(db.Float)
    geography_score = db.Column(db.Float)
    philosophy_score = db.Column(db.Float)
    art_score = db.Column(db.Float)
    foreign_language_score = db.Column(db.Float)
    
    def to_dict(self):
        return {
            "id": self.id,
            "math_score": self.math_score,
            "physics_score": self.physics_score,
            "chemistry_score": self.chemistry_score,
            "biology_score": self.biology_score,
            "literature_score": self.literature_score,
            "history_score": self.history_score,
            "geography_score": self.geography_score,
            "philosophy_score": self.philosophy_score,
            "art_score": self.art_score,
            "foreign_language_score": self.foreign_language_score
        }


class Volunteer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    school_performance_id = db.Column(db.Integer, db.ForeignKey('student.id'))
    job_name = db.Column(db.String(100))

class JobEarnings(db.Model):
    job_name = db.Column(db.String(100), primary_key=True)
    average_earnings = db.Column(db.Float)