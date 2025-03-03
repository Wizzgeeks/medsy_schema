from mongoengine import Document,ReferenceField,DictField,StringField,BooleanField,DateTimeField
from Models.user_model import User
from Models.component_model import Component
from Models.course_model import Course
from Models.layer_1_model import Layer_1
from Models.layer_2_model import Layer_2
from Models.layer_3_model import Layer_3
from Models.model_model import Model
from Models.subject_model import Subject


class Component_completed(Document):
    
    course = ReferenceField(Course,required=True,reverse_delete_rule=2)
    subject=ReferenceField(Subject,required=True,reverse_delete_rule=2)
    component=ReferenceField(Component,required=True,reverse_delete_rule=2)
    layer1 = ReferenceField(Layer_1,reverse_delete_rule=2)
    layer2 = ReferenceField(Layer_2,reverse_delete_rule=2)
    layer3 = ReferenceField(Layer_3,reverse_delete_rule=2)
    user = ReferenceField(User,required=True,reverse_delete_rule=2)
    completed=BooleanField(required=True)


    def to_json(self):
        return {
            "course":str(self.course),
            "subject":str(self.subject.id) if self.subject.id else None,
            "component":self.component.to_json if self.component else None,
            "layer1":str(self.layer1.id) if self.layer1 else None,
            "layer2":str(self.layer2.id) if self.layer2 else None,
            "layer3":str(self.layer3.id) if self.layer3 else None,
            "user":str(self.user.id) if self.user else None,
            "completed":self.completed
        }