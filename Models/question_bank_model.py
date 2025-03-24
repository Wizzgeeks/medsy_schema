from Models.course_model import Course
from Models.subject_model import Subject
from Models.layer_1_model import Layer_1
from Models.layer_2_model import Layer_2
from Models.layer_3_model import Layer_3
from mongoengine  import Document,StringField,IntField,ReferenceField,DateTimeField,ListField,DictField

class Question_bank(Document):
    course=ReferenceField(Course,reverse_delete_rule=2,required=True)
    subject=ReferenceField(Subject,reverse_delete_rule=2)
    layer1=ReferenceField(Layer_1,reverse_delete_rule=2)
    layer2=ReferenceField(Layer_2,reverse_delete_rule=2)
    layer3=ReferenceField(Layer_3,reverse_delete_rule=2)
    question_bank_content=ListField(DictField())

    def to_json(self):
        return {
            "id":str(self.id),
            'course':str(self.course.id),
            'subject':str(self.subject.id),
            'layer1':str(self.layer1.id) if self.layer1 else None,
            'layer2':str(self.layer2.id) if self.layer2 else None,
            'layer3':str(self.layer3.id) if self.layer3 else None,
            'question_bank_content':self.question_bank_content
        }