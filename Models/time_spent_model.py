from mongoengine import Document,ReferenceField,StringField,ValidationError,ListField
from Models.layer_3_model import Layer_3
from Models.user_model import User
from Models.course_model import Course
from Models.layer_1_model import Layer_1
from Models.subject_model import Subject
from Models.layer_2_model import Layer_2
from Models.layer_3_model import Layer_3
from Models.year_model import Year


class Time_spent(Document):
    course = ReferenceField(Course,reverse_delete_rule=2)
    year = ReferenceField(Year,reverse_delete_rule=2)
    subject = ReferenceField(Subject,reverse_delete_rule=2)
    layer1 = ReferenceField(Layer_1,reverse_delete_rule=2)
    layer2 = ReferenceField(Layer_2reverse_delete_rule=2)
    layer3 = ReferenceField(Layer_3,reverse_delete_rule=2)
    layer3 = StringField(required=True)
    user = ReferenceField(User,required=True,reverse_delete_rule=2)
    time_spent = StringField()

    def to_json(self):
        return {
            "id":str(self.id),
            "layer3":str(self.layer3.id) if self.layer3 else None,
            "user":str(self.user.id) if self.user else None,
            "time_spent":self.time_spent,
        }
    
    def with_key(self):
        return {
            "id":str(self.id),
            "layer3":self.layer3.to_json() if self.layer3 else None,
            "user":self.user.to_json() if self.user else None,
            "time_spent":self.time_spent,
        }
    
    def clean(self):
        if not self.time_spent:
            raise ValidationError("Time spent Cannot be empty")
        
    def update(self, **kwargs):
        self.clean()
        return super().update(**kwargs)
