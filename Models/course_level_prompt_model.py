from mongoengine import Document,ReferenceField,DictField,StringField,BooleanField,DateTimeField,CASCADE
from Models.component_model import Component
from Models.course_model import Course
from Models.layer_1_model import Layer_1
from Models.layer_2_model import Layer_2
from Models.layer_3_model import Layer_3
from Models.model_model import Model
from Models.subject_model import Subject
from Models.year_model import Year
from datetime import datetime,timezone 

class Course_level_prompt(Document):
    course = ReferenceField(Course,reverse_delete_rule=CASCADE,required=True)
    model = ReferenceField(Model,reverse_delete_rule=CASCADE,required=True)
    # year = ReferenceField(Year,reverse_delete_rule=CASCADE)
    # subject = ReferenceField(Subject,reverse_delete_rule=CASCADE)
    # layer1 = ReferenceField(Layer_1,reverse_delete_rule=CASCADE)
    # layer2 = ReferenceField(Layer_2,reverse_delete_rule=CASCADE)
    # layer3 = ReferenceField(Layer_3,reverse_delete_rule=CASCADE)
    component = ReferenceField(Component,reverse_delete_rule=CASCADE)
    createdAt=DateTimeField(required=True,default=datetime.now(timezone.utc))
    prompt_framework = DictField(required=True)
    isCurrent=BooleanField(required=True,default=True)
    name=StringField()
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
            "isCurrent":self.isCurrent,
            "name":self.name
        }
        