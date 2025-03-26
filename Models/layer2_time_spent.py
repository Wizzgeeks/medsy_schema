from mongoengine import Document,ReferenceField,IntField,DictField,ListField,StringField,BooleanField
from Models.user_model import User
from Models.layer_1_model import Layer_1
from Models.course_model import Course
from Models.subject_model import Subject
from Models.layer_2_model import Layer_2
# from Models.layer_3_model import Layer_3
from Models.layer2_page_model import Layer2_page

class Layer1_time_spent(Document):
    coures = ReferenceField(Course,required=True,reverse_delete_rule=2)
    subject = ReferenceField(Subject,required=True,reverse_delete_rule=2)
    layer1 = ReferenceField(Layer_1,reverse_delete_rule=2)
    layer2=ReferenceField(Layer_2,required=True,reverse_delete_rule=2)
    user = ReferenceField(User,required=True,reverse_delete_rule=2)
    layer2_page = ReferenceField(Layer2_page,required=True,reverse_delete_rule=2)
    attempts =ListField(DictField())
    types=StringField(choices=['mcq','test_series','ctc_fillups','ctc_mcq','ctc_analysis','content'],required=True)
    completed=BooleanField(default=False)
    

    def to_json(self):
        return {
            # "layer1":str(self.layer1.id) if self.layer1 else None,
            # "user":str(self.user.id) if self.user else None,
            # "coures":str(self.coures.id) if self.coures else None,
            # "subject":str(self.subject.id) if self.subject else None,
            "user":self.user.to_json() if self.user else None,
            "coures":self.coures.to_json() if self.coures else None,
            "subject":self.subject.to_json() if self.subject else None,
            "layer1":self.layer1.to_json() if self.layer1 else None,
            "layer2":self.layer2.to_json() if self.layer2 else None,
            "layer2_page":self.layer2_page.to_json() if self.layer2_page else None,
            "attempts":self.attempts,
            "types":self.types,
            "completed":self.completed
            }