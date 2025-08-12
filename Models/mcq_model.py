from mongoengine import Document, ReferenceField,ListField,DictField,StringField,BooleanField,IntField,CASCADE
# from Models.course_model import Course
# from Models.subject_model import Subject
# from Models.layer_1_model import Layer_1
# from Models.layer_2_model import Layer_2
# from Models.layer_3_model import Layer_3
from Models.layer1_page_model import Layer1_page
from Models.layer2_page_model import Layer2_page
from Models.layer3_page_model import Layer3_page
from Models.subject_page_model import Subject_page
from Models.year_model import Year
from Models.user_model import User


class Mcq_result(Document):
    user=ReferenceField(User,reverse_delete_rule=CASCADE,required=True)
    layer1_page = ReferenceField(Layer1_page, reverse_delete_rule=CASCADE, null=True)
    layer2_page = ReferenceField(Layer2_page, reverse_delete_rule=CASCADE, null=True)
    layer3_page = ReferenceField(Layer3_page, reverse_delete_rule=CASCADE, null=True)
    subject_page=ReferenceField(Subject_page, reverse_delete_rule=CASCADE, null=True)
    attempt_data = ListField(DictField())
    score=IntField()
    total_questions=IntField()
    attempt_questions=IntField()
    time_taken=IntField()
    completed=BooleanField(default=False)
    

    def to_json(self):
        return {
            "id": str(self.id),
            "user":str(self.user.id) if self.user else None,
            "layer1_page": str(self.layer1_page.id) if self.layer1_page else None,
            "layer2_page": str(self.layer2_page.id) if self.layer2_page else None,
            "layer3_page": str(self.layer3_page.id) if self.layer3_page else None,
            "attempt_data": self.attempt_data,
            "completed":self.completed,
            "score":self.score,
            "total_questions":self.total_questions,
            "attempt_questions":self.attempt_questions,
            "time_taken":self.time_taken
        }
    
    def to_user(self):
        return {
            "id": str(self.id),
            "user":str(self.user.id) if self.user else None,            
            "layer1_page": str(self.layer1_page.id) if self.layer1_page else None,
            "layer2_page": str(self.layer2_page.id) if self.layer2_page else None,
            "layer3_page": str(self.layer3_page.id) if self.layer3_page else None,
            "attempt_data": self.attempt_data,
            "completed":self.completed,
            "score":self.score,
            "total_questions":self.total_questions,
            "attempt_questions":self.attempt_questions,
            "time_taken":self.time_taken
        }
