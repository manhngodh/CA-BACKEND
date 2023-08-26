from marshmallow import Schema, fields, validates, ValidationError

class JobDataSchema(Schema):
    job_title = fields.String(required=True)
    description = fields.String(required=True)
    skills = fields.List(fields.String(), required=True)

class ListJobDataSchema(Schema):
    jobs = fields.List(fields.Nested(JobDataSchema), required=True)

    @validates('jobs')
    def validate_job_data(self, jobs):
        if not jobs:
            raise ValidationError('At least one job data entry is required')


class SchoolPerformanceSchema(Schema):
    math = fields.Float(required=False)
    physics = fields.Float(required=False)
    chemistry = fields.Float(required=False)
    biology = fields.Float(required=False)
    literature = fields.Float(required=False)
    history = fields.Float(required=False)
    geography = fields.Float(required=False)
    philosophy = fields.Float(required=False)
    art = fields.Float(required=False)
    foreign_language = fields.Float(required=False)