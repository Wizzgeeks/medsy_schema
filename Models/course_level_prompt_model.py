from mongoengine import Document,ReferenceField,DictField,StringField,BooleanField,DateTimeField
from Models.component_model import Component
from Models.course_model import Course
from Models.layer_1_model import Layer_1
from Models.layer_2_model import Layer_2
from Models.layer_3_model import Layer_3
from Models.model_model import Model
from Models.subject_model import Subject
from Models.year_model import Year
from datetime import datetime 

class Course_level_prompt(Document):
    course = ReferenceField(Course,required=True,reverse_delete_rule=2)
    model = ReferenceField(Model,required=True,reverse_delete_rule=2)
    # year = ReferenceField(Year,reverse_delete_rule=2)
    # subject = ReferenceField(Subject,reverse_delete_rule=2)
    # layer1 = ReferenceField(Layer_1,reverse_delete_rule=2)
    # layer2 = ReferenceField(Layer_2,reverse_delete_rule=2)
    # layer3 = ReferenceField(Layer_3,reverse_delete_rule=2)
    component = ReferenceField(Component,reverse_delete_rule=2)
    createdAt=DateTimeField(required=True,default=datetime.now())
    prompt_framework = DictField(required=True)
    isCurrent=BooleanField(required=True,default=True)
    
    def to_json(self):
        return {
            "id": str(self.id),
            "course":str(self.course.id) if self.course else None,
            "model":str(self.model.id) if self.model else None,
            # "year":str(self.year.id) if self.year else None,
            # "subject":str(self.subject.id) if self.subject else None,
            # "layer1":str(self.layer1.id) if self.layer1 else None,
            # "layer2":str(self.layer2.id) if self.layer2 else None,
            # "layer3":str(self.layer3.id) if self.layer3 else None,
            "component":str(self.component.id) if self.component else None,
            "createdAt":str(self.createdAt),
            "prompt_framework":self.prompt_framework,
            "isCurrent":self.isCurrent
        }
        