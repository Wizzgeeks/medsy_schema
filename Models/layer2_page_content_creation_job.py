from mongoengine import Document,StringField,IntField,ReferenceField,DateTimeField,ListField,DictField
from Models.job_detail import Job_detail
from Models.course_model import Course
from Models.subject_model import Subject
from Models.layer_1_model import Layer_1
from Models.layer_2_model import Layer_2
from Models.year_model import Year
from datetime import datetime
class Layer2_page_creation_job(Document):
    job_id=ReferenceField(Job_detail,reverse_delete_rule=2,required=True)
    course = ReferenceField(Course,reverse_delete_rule=2,required=True)
    year = ReferenceField(Year,reverse_delete_rule=2,required=True)
    subject = ReferenceField(Subject,reverse_delete_rule=2,required=True)
    layer1 = ReferenceField(Layer_1,reverse_delete_rule=2)
    layer2 = ReferenceField(Layer_2,reverse_delete_rule=2,required=True)
    logs=ListField(DictField())
    conversation = ListField(default=[])
    created_at=DateTimeField(default=datetime.now,required=True)
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
            'logs':self.logs,
            'conversation':self.conversation if self.conversation else [],
            'created_at':self.created_at
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
            'logs':self.logs,
            'conversation':self.conversation if self.conversation else [],
            'created_at':self.created_at
            }