from mongoengine import Document,ReferenceField,BooleanField,CASCADE,IntField,ListField,DictField,CASCADE
from Models.user_model import User
from Models.layer_3_model import Layer_3
from Models.layer_2_model import Layer_2
from Models.layer_1_model import Layer_1
from Models.subject_model import Subject
from Models.year_model import Year
from Models.course_model import Course


def get_default_mastery():
    return {
        "direct": {
            "total": 0,
            "scored": 0
        },
        "critical_thinking": {
            "total": 0,
            "scored": 0
        },
        "reasoning": {
            "total": 0,
            "scored": 0
        },
        "application": {
            "total": 0,
            "scored": 0
        }
    }

class Layer3_completion_status(Document):
    course=ReferenceField(Course,reverse_delete_rule=CASCADE,required=True)
    year=ReferenceField(Year,reverse_delete_rule=CASCADE,required=True)
    subject=ReferenceField(Subject,reverse_delete_rule=CASCADE,required=True)
    layer1=ReferenceField(Layer_1,reverse_delete_rule=CASCADE)
    layer2=ReferenceField(Layer_2,reverse_delete_rule=CASCADE,required=True)
    layer3 = ReferenceField(Layer_3,reverse_delete_rule=CASCADE,required=True)
    user = ReferenceField(User,reverse_delete_rule=CASCADE,required=True)
    completed=BooleanField(default=False)
    total_page=IntField()
    completed_page=IntField()
    time_taken_page=IntField()
    mastery_l3 =DictField(default=lambda: get_default_mastery())


    def to_json(self):
        return {
            "id":str(self.id),
            "course":str(self.course.id) if self.course else None,
            "year":str(self.year.id) if self.year else None,
            "subject":str(self.subject.id) if self.subject else None,
            "layer1":str(self.layer1.id) if self.layer1 else None,
            "layer2":str(self.layer2.id) if self.layer2 else None,
            "layer3":str(self.layer3.id) if self.layer3 else None,
            "user":str(self.user.id) if self.user else None,
            "completed":self.completed if self.completed else 0,
            "total_page":self.total_page if self.total_page else 0 ,
            "completed_page":self.completed_page if self.completed_page else 0,
        }
    
    def with_key(self):
        return {
            "id":str(self.id),
            "course":self.course.to_json() if self.course else None,
            "year":self.year.to_json() if self.year else None,
            "subject":self.subject.to_json() if self.subject else None,
            "layer1":self.layer1.to_json() if self.layer1 else None,
            "layer2":self.layer2.to_json() if self.layer2 else None,
            "layer3":self.layer3.to_json() if self.layer3 else None,
            "user":str(self.user.id) if self.user else None,
            "completed":self.completed if self.completed else 0,
            "total_page":self.total_page if self.total_page else 0 ,
            "completed_page":self.completed_page if self.completed_page else 0,
        }
    