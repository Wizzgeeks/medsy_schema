from Models.prompt_ctc_job import Prompt_ctc_job
from Models.course_model import Course
from Models.subject_model import Subject
from Models.year_model import Year
from mongoengine import Document,StringField,ReferenceField,DateTimeField,CASCADE
from datetime import datetime,timezone

class Subject_prompt_ctc_apply_job(Document):
    job_id=ReferenceField(Prompt_ctc_job,reverse_delete_rule=CASCADE,required=True)
    course = ReferenceField(Course,reverse_delete_rule=CASCADE,required=True)
    year = ReferenceField(Year,reverse_delete_rule=CASCADE,required=True)
    subject = ReferenceField(Subject,reverse_delete_rule=CASCADE,required=True)
    created_at=DateTimeField(default=datetime.now(timezone.utc),required=True)
    updated_at = DateTimeField(null=True)
    status=StringField()

    def to_json(self):
        return {
            "id":str(self.id),
            'job_id':self.job_id.to_json(),
            'course':str(self.course.id),
            'year':str(self.year.id),
            'subject':self.subject.to_json(),
            'status':self.status,
            'updated_at':str(self.updated_at) if self.updated_at else None,
            'created_at':str(self.created_at)
            }
    
    def to_admin(self):
        return {
            "id":str(self.id),
            'job_id':str(self.job_id.id),
            'course':str(self.course.id),
            'year':str(self.year.id),
            'subject':self.subject.to_json(),
            'status':self.status,
            'updated_at':str(self.updated_at) if self.updated_at else None,
            'created_at':str(self.created_at)
            }