from Models.prompt_ctc_job import Prompt_ctc_job
from Models.course_model import Course
from Models.subject_model import Subject
from Models.year_model import Year
from mongoengine import Document,StringField,ReferenceField,DateTimeField
from datetime import datetime,timezone

class Subject_prompt_ctc_apply_job(Document):
    job_id=ReferenceField(Prompt_ctc_job,reverse_delete_rule=2,required=True)
    course = ReferenceField(Course,reverse_delete_rule=2,required=True)
    year = ReferenceField(Year,reverse_delete_rule=2,required=True)
    subject = ReferenceField(Subject,reverse_delete_rule=2,required=True)
    created_at=DateTimeField(default=datetime.now(),required=True)
    updated_at = DateTimeField(null=True)
    status=StringField()

    def to_json(self):
        return {
            "id":str(self.id),
            'job_id':self.job_id.to_json(),
            'course':str(self.course.id),
            'year':str(self.year.id),
            'subject':str(self.subject.id),
            'status':self.status,
            'updated_at':str(self.updated_at) if self.updated_at else None,
            'created_at':self.created_at
            }
    
    def to_admin(self):
        return {
            "id":str(self.id),
            'job_id':str(self.job_id.id),
            'course':str(self.course.id),
            'year':str(self.year.id),
            'subject':str(self.subject.id),
            'status':self.status,
            'updated_at':str(self.updated_at) if self.updated_at else None,
            'created_at':self.created_at
            }