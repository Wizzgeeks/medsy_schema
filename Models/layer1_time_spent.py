from mongoengine import Document,ReferenceField,IntField,DictField,ListField,StringField,BooleanField
from Models.user_model import User
from Models.layer_1_model import Layer_1
from Models.course_model import Course
from Models.subject_model import Subject
from Models.layer1_page_model import Layer1_page
from Models.year_model import Year
class Layer1_time_spent(Document):
    course = ReferenceField(Course,required=True,reverse_delete_rule=2)
    year = ReferenceField(Year,required=True,reverse_delete_rule=2)
    subject = ReferenceField(Subject,required=True,reverse_delete_rule=2)
    layer1 = ReferenceField(Layer_1,required=True,reverse_delete_rule=2)
    user = ReferenceField(User,required=True,reverse_delete_rule=2)
    layer1_page = ReferenceField(Layer1_page,required=True,reverse_delete_rule=2)
    attempts =ListField(DictField())
    types=StringField(choices=['mcq','test_series','ctc_fillups','ctc_mcq','ctc_analysis','content','exam'],required=True)
    completed=BooleanField(default=False)
    child=BooleanField(default=False) 
    parent=BooleanField(default=False) 
    


    def to_json(self):
        return {
            # "layer1":str(self.layer1.id) if self.layer1 else None,
            # "user":str(self.user.id) if self.user else None,
            # "course":str(self.course.id) if self.course else None,
            # "subject":str(self.subject.id) if self.subject else None,
            "layer1":self.layer1.to_json() if self.layer1 else None,
            "user":self.user.to_json() if self.user else None,
            "course":self.course.to_json() if self.course else None,
            "subject":self.subject.to_json() if self.subject else None,
            "year":self.year.to_json() if self.year else None,
            "layer1_page":self.layer1_page.to_json() if self.layer1_page else None,
            "attempts":self.attempts,
            "types":self.types,
            "completed":self.completed,
            "child": self.child,
            "parent": self.parent
            }