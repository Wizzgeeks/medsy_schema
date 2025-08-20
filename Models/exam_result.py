from mongoengine  import Document,ReferenceField,ListField,DictField,GenericReferenceField,StringField,IntField,CASCADE
from Models.course_model import Course
from Models.subject_model import Subject
from Models.layer_1_model import Layer_1
from Models.layer_2_model import Layer_2
from Models.layer_3_model import Layer_3
from Models.year_model import Year
from Models.user_model import User


class Exam_results(Document):
    course=ReferenceField(Course,reverse_delete_rule=CASCADE,required=True)
    user=ReferenceField(User,reverse_delete_rule=CASCADE,required=True)
    year=ReferenceField(Year,reverse_delete_rule=CASCADE,required=True)
    subject=ReferenceField(Subject,reverse_delete_rule=CASCADE)
    layer1=ReferenceField(Layer_1,reverse_delete_rule=CASCADE)
    layer2=ReferenceField(Layer_2,reverse_delete_rule=CASCADE)
    layer3=ReferenceField(Layer_3,reverse_delete_rule=CASCADE)
    page = GenericReferenceField(required=True)
    result=ListField(DictField())
    status = StringField()
    total_mark = IntField()

    def to_json(self):
        return {
            "id":str(self.id),
            'course':str(self.course.id),
            'user':str(self.user.id),
            'year': str(self.year.id) if self.year else None,
            'subject':str(self.subject.id),
            'layer1':str(self.layer1.id) if self.layer1 else None,
            'layer2':str(self.layer2.id) if self.layer2 else None,
            'layer3':str(self.layer3.id) if self.layer3 else None,
            'result':self.result,
            "page": str(self.page.id) if self.page else None,
            'status':self.status if self.status else None,
            "total_mark":self.total_mark if self.total_mark else 0
        }
    
    def to_user(self):
        return {
            "id": str(self.id),
            'user':str(self.user.id),
            'course': str(self.course.id) if self.course else None,
            'year': str(self.year.id) if self.year else None,
            "subject": str(self.subject.id) if self.subject else None,
            "layer1": str(self.layer1.id) if self.layer1 else None,
            "layer2": str(self.layer2.id) if self.layer2 else None,
            "layer3": str(self.layer3.id) if self.layer3 else None,
            "page": str(self.page.id) if self.page else None,
            'result':self.result,
            'status':self.status if self.status else None,
            "total_mark":self.total_mark if self.total_mark else 0

        }