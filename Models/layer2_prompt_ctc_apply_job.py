from mongoengine import Document,StringField,IntField,ReferenceField,DateTimeField,ListField,DictField,CASCADE
from Models.prompt_ctc_job import Prompt_ctc_job
from Models.course_model import Course
from Models.subject_model import Subject
from Models.layer_1_model import Layer_1
from Models.layer_2_model import Layer_2
from Models.year_model import Year
from datetime import datetime,timezone

class Layer2_prompt_ctc_apply_job(Document):
    job_id=ReferenceField(Prompt_ctc_job,reverse_delete_rule=CASCADE,required=True)
    course = ReferenceField(Course,reverse_delete_rule=CASCADE,required=True)
    year = ReferenceField(Year,reverse_delete_rule=CASCADE,required=True)
    subject = ReferenceField(Subject,reverse_delete_rule=CASCADE,required=True)
    layer1 = ReferenceField(Layer_1,reverse_delete_rule=CASCADE)
    layer2 = ReferenceField(Layer_2,reverse_delete_rule=CASCADE,required=True)
    created_at=DateTimeField(default=datetime.now(timezone.utc),required=True)
    updated_at = DateTimeField(null=True)
    status=StringField()

    def to_json(self):
        return {
            "id":str(self.id),
            'job_id':self.job_id.to_json(),
            'course':str(self.course.id),
            'year':str(self.year.id),
            'subject':str(self.subject.id),
            'layer1':str(self.layer1.id) if self.layer1 else None,
            'layer2':self.layer2.to_json(),
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
            'subject':str(self.subject.id),
            'layer1':str(self.layer1.id) if self.layer1 else None,
            'layer2':self.layer2.to_json(),
            'status':self.status,
            'updated_at':str(self.updated_at) if self.updated_at else None,
            'created_at':str(self.created_at)
            }