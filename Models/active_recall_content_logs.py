from mongoengine import Document,StringField,ReferenceField,DateTimeField,ListField,DictField,CASCADE
from Models.course_model import Course
from Models.subject_model import Subject
from Models.layer_1_model import Layer_1
from Models.layer_2_model import Layer_2
from Models.layer_3_model import Layer_3
from Models.year_model import Year
from datetime import datetime,timezone
from Models.user_model import User
from Models.active_recall_content import Active_recall_content
from Models.active_recall import Active_recall


class Active_recall_content_logs(Document):
    active = ReferenceField(Active_recall,reverse_delete_rule=CASCADE)
    active_content = ReferenceField(Active_recall_content,reverse_delete_rule=CASCADE)
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
            'active':str(self.active.id) if self.active else None,
            'active_content':str(self.active_content.id) if self.active_content else None,
            'user': str(self.user.id) if self.user else None,
            'course':str(self.course.id),
            'year':str(self.year.id),
            'subject':str(self.subject.id) if self.subject else None,
            'layer1':str(self.layer1.id) if self.layer1 else None,
            'layer2':str(self.layer2.id) if self.layer2 else None,
            'layer3':str(self.layer3.id) if self.layer3 else None,
            "layer":self.layer if self.layer else None,
            'status':self.status,
            'logs':self.logs,
            'conversation':self.conversation if self.conversation else [],
            'updated_at':str(self.updated_at) if self.updated_at else None,
            'created_at':str(self.created_at)
            }
