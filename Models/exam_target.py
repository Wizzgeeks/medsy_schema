from Models.course_model import Course
from Models.year_model import Year
from mongoengine import Document, StringField, ReferenceField, GenericReferenceField, DateTimeField, ListField,CASCADE
from datetime import datetime
from Models.subject_model import Subject
from Models.layer_1_model import Layer_1
from Models.layer_2_model import Layer_2
from Models.layer_3_model import Layer_3
from Models.layer1_page_model import Layer1_page
from Models.layer2_page_model import Layer2_page
from Models.layer3_page_model import Layer3_page
from Models.subject_page_model import Subject_page

class Exam_target(Document):
    course = ReferenceField(Course, reverse_delete_rule=CASCADE, required=True)
    year = ReferenceField(Year, reverse_delete_rule=CASCADE, required=True)
    layer = StringField(choices=['subject', 'layer1', 'layer2', 'layer3'], required=True)
    subject=ReferenceField(Subject,reverse_delete_rule=CASCADE)
    layer1=ReferenceField(Layer_1,reverse_delete_rule=CASCADE)
    layer2=ReferenceField(Layer_2,reverse_delete_rule=CASCADE)
    layer3=ReferenceField(Layer_3,reverse_delete_rule=CASCADE)
    layer1_page = ReferenceField(Layer1_page, reverse_delete_rule=CASCADE, null=True)
    layer2_page = ReferenceField(Layer2_page, reverse_delete_rule=CASCADE, null=True)
    layer3_page = ReferenceField(Layer3_page, reverse_delete_rule=CASCADE, null=True)
    subject_page=ReferenceField(Subject_page,reverse_delete_rule=CASCADE, null=True)
    target = ListField(GenericReferenceField(required=True), required=True)
    # page = GenericReferenceField(required=True)
    created_at = DateTimeField(default=datetime.now, required=True)
    updated_at = DateTimeField(null=True)

    def to_json(self):
        return {
            "id": str(self.id),
            "course": str(self.course.id),
            "year": str(self.year.id),
            'subject':str(self.subject.id) if self.subject else None,
            'layer1':str(self.layer1.id) if self.layer1 else None,
            'layer2':str(self.layer2.id) if self.layer2 else None,
            'layer3':str(self.layer3.id) if self.layer3 else None,
            "layer1_page": str(self.layer1_page.id) if self.layer1_page else None,
            "layer2_page": str(self.layer2_page.id) if self.layer2_page else None,
            "layer3_page": str(self.layer3_page.id) if self.layer3_page else None,
            "subject_page":str(self.subject_page.id) if self.subject_page else None,
            "layer": self.layer,
            "target": [t.to_json() for t in self.target] if self.target else None,
            # "page": str(self.page.id) if self.page else None,
            "updated_at": str(self.updated_at) if self.updated_at else None,
            "created_at": str(self.created_at),
        }
