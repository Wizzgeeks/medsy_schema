from Models.prompt_job_model import Prompt_job
from Models.course_model import Course
from Models.subject_model import Subject
from Models.layer_1_model import Layer_1
from Models.year_model import Year
from mongoengine import Document,StringField,IntField,ReferenceField,DateTimeField,ListField,DictField
from datetime import datetime,timezone

class Layer1_prompt_apply_job(Document):
    job_id=ReferenceField(Prompt_job,reverse_delete_rule=2,required=True)
    course = ReferenceField(Course,reverse_delete_rule=2,required=True)
    year = ReferenceField(Year,reverse_delete_rule=2,required=True)
    subject = ReferenceField(Subject,reverse_delete_rule=2,required=True)
    layer1 = ReferenceField(Layer_1,reverse_delete_rule=2,required=True)
    created_at=DateTimeField(default=datetime.now(timezone.utc),required=True)
    updated_at=DateTimeField(null=True)
    status=StringField()

    def to_json(self):
        return {
            "id":str(self.id),
            'job_id':self.job_id.to_json(),
            'course':str(self.course.id),
            'year':str(self.year.id),
            'subject':str(self.subject.id),
            'layer1':self.layer1.to_json(),
            'status':self.status,
            'created_at':str(self.created_at),
            'updated_at':str(self.updated_at) if self.updated_at else None,

            }
    
    def to_admin(self):
        return {
            "id":str(self.id),
            'job_id':str(self.job_id.id),
            'course':str(self.course.id),
            'year':str(self.year.id),
            'subject':str(self.subject.id),
            'layer1':self.layer1.to_json(),
            'status':self.status,
            'created_at':str(self.created_at),
            'updated_at':str(self.updated_at) if self.updated_at else None,
            }