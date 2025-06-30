from mongoengine import Document,StringField,ReferenceField,DateTimeField,ListField,DictField
from Models.course_model import Course
from Models.subject_model import Subject
from Models.layer_1_model import Layer_1
from Models.layer_2_model import Layer_2
from Models.layer_3_model import Layer_3
from Models.layer1_page_model import Layer1_page
from Models.layer2_page_model import Layer2_page
from Models.layer3_page_model import Layer3_page
from Models.subject_page_model import Subject_page
from Models.year_model import Year
from datetime import datetime,timezone
from Models.active_recall_mcq import Active_recall_mcq
from Models.active_recall import Active_recall


class Active_recall_mcq_logs(Document):
    active = ReferenceField(Active_recall,reverse_delete_rule=2)
    active_mcq = ReferenceField(Active_recall_mcq,reverse_delete_rule=2)
    course = ReferenceField(Course,reverse_delete_rule=2,required=True)
    year = ReferenceField(Year,reverse_delete_rule=2,required=True)
    subject = ReferenceField(Subject,reverse_delete_rule=2)
    layer1 = ReferenceField(Layer_1,reverse_delete_rule=2)
    layer2 = ReferenceField(Layer_2,reverse_delete_rule=2)
    layer3 = ReferenceField(Layer_3,reverse_delete_rule=2)
    layer1_page = ReferenceField(Layer1_page, reverse_delete_rule=2, null=True)
    layer2_page = ReferenceField(Layer2_page, reverse_delete_rule=2, null=True)
    layer3_page = ReferenceField(Layer3_page, reverse_delete_rule=2, null=True)
    subject_page=ReferenceField(Subject_page,reverse_delete_rule=2, null=True)
    logs=ListField(DictField())
    conversation = ListField(default=[])
    created_at=DateTimeField(default=datetime.now(timezone.utc))
    updated_at = DateTimeField(null=True)
    status=StringField()

    def to_json(self):
        return {
            "id":str(self.id),
            'active':str(self.active.id) if self.active else None,
            'active_mcq':str(self.active_mcq.id) if self.active_mcq else None,
            'course':str(self.course.id),
            'year':str(self.year.id),
            'subject':str(self.subject.id) if self.subject else None,
            'layer1':str(self.layer1.id) if self.layer1 else None,
            'layer2':str(self.layer2.id) if self.layer2 else None,
            'layer3':str(self.layer3.id) if self.layer3 else None,
            "layer1_page": str(self.layer1_page.id) if self.layer1_page else None,
            "layer2_page": str(self.layer2_page.id) if self.layer2_page else None,
            "layer3_page": str(self.layer3_page.id) if self.layer3_page else None,
            "subject_page":str(self.subject_page.id) if self.subject_page else None,
            'status':self.status,
            'logs':self.logs,
            'conversation':self.conversation if self.conversation else [],
            'updated_at':str(self.updated_at) if self.updated_at else None,
            'created_at':str(self.created_at)
            }
