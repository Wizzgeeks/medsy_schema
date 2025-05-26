from Models.course_model import Course
from Models.subject_model import Subject
from Models.layer_1_model import Layer_1
from Models.layer_2_model import Layer_2
from Models.layer_3_model import Layer_3
from Models.year_model import Year
from mongoengine import Document,StringField,ReferenceField,DateTimeField,ListField
from datetime import datetime

class Exam_target(Document):
    course = ReferenceField(Course,reverse_delete_rule=2,required=True)
    year = ReferenceField(Year,reverse_delete_rule=2,required=True)
    layer = StringField(choices=['subject','layer1','layer2','layer3'],required=True)
    target =ListField(ReferenceField(choices=[Subject,Layer_1,Layer_2,Layer_3],reverse_delete_rule=2),required=True)
    created_at=DateTimeField(default=datetime.now(),required=True)
    updated_at=DateTimeField(null=True)

    def to_json(self):
        return {
            "id":str(self.id),
            'course':str(self.course.id),
            'year':str(self.year.id),
            'layer':self.layer,
            'target':[targets.to_json() for targets in self.target] if self.target else None,
            'updated_at':str(self.updated_at) if self.updated_at else None,
            'created_at':str(self.created_at),
            }
    
