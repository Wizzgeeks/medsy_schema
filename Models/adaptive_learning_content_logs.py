from mongoengine import Document,StringField,ReferenceField,DateTimeField,ListField,DictField,CASCADE
from Models.course_model import Course
from Models.subject_model import Subject
from Models.layer_1_model import Layer_1
from Models.layer_2_model import Layer_2
from Models.layer_3_model import Layer_3
from Models.year_model import Year
from datetime import datetime,timezone
from Models.adaptive_page_content import Adaptive_learning_content
from Models.adaptive_learning_page import Adaptive_learning
from Models.user_model import User



class Adaptive_learning_content_logs(Document):
    adaptive=ReferenceField(Adaptive_learning,reverse_delete_rule=CASCADE)
    adaptive_content=ReferenceField(Adaptive_learning_content,reverse_delete_rule=CASCADE)
    user = ReferenceField(User, reverse_delete_rule=CASCADE, required=True)
    course = ReferenceField(Course,reverse_delete_rule=CASCADE,required=True)
    year = ReferenceField(Year,reverse_delete_rule=CASCADE,required=True)
    subject = ReferenceField(Subject,reverse_delete_rule=CASCADE)
    layer1 = ReferenceField(Layer_1,reverse_delete_rule=CASCADE)
    layer2 = ReferenceField(Layer_2,reverse_delete_rule=CASCADE)
    layer3 = ReferenceField(Layer_3,reverse_delete_rule=CASCADE)
    layer = StringField(choices=['subject', 'layer1', 'layer2', 'layer3'], required=True)
    logs=ListField(DictField())
    conversation = ListField(default=[])
    created_at=DateTimeField(default=datetime.now(timezone.utc))
    updated_at = DateTimeField(null=True)
    status=StringField()

    def to_json(self):
        return {
            "id":str(self.id),
            'adaptive':str(self.adaptive.id )if self.adaptive else None,
            'adaptive_content':str(self.adaptive_content.id )if self.adaptive_content else None,
            'user': str(self.user.id) if self.user else None,
            'course':str(self.course.id),
            'year':str(self.year.id),
            'subject':str(self.subject.id) if self.subject else None,
            'layer1':str(self.layer1.id) if self.layer1 else None,
            'layer2':str(self.layer2.id) if self.layer2 else None,
            'layer3':str(self.layer3.id) if self.layer3 else None,
            "layer":self.layer if self.layer else None,
            'status':self.status,
            'logs_content':self.logs,
            'logs_mcq':self.logs,
            'conversation_mcq':self.conversation if self.conversation else [],
            'updated_at':str(self.updated_at) if self.updated_at else None,
            'created_at':str(self.created_at)
            }
