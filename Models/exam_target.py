from Models.course_model import Course
from Models.year_model import Year
from mongoengine import Document, StringField, ReferenceField, GenericReferenceField, DateTimeField, ListField
from datetime import datetime

class Exam_target(Document):
    course = ReferenceField(Course, reverse_delete_rule=2, required=True)
    year = ReferenceField(Year, reverse_delete_rule=2, required=True)
    layer = StringField(choices=['subject', 'layer1', 'layer2', 'layer3'], required=True)
    target = ListField(GenericReferenceField(required=True), required=True)
    page = GenericReferenceField(required=True)
    created_at = DateTimeField(default=datetime.now, required=True)
    updated_at = DateTimeField(null=True)

    def to_json(self):
        return {
            "id": str(self.id),
            "course": str(self.course.id),
            "year": str(self.year.id),
            "layer": self.layer,
            "target": [t.to_json() for t in self.target] if self.target else None,
            "page": str(self.page.id) if self.page else None,
            "updated_at": str(self.updated_at) if self.updated_at else None,
            "created_at": str(self.created_at),
        }
