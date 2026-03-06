from mongoengine import (Document, StringField, ReferenceField, ListField, DateTimeField,
                         IntField, BooleanField, CASCADE, NULLIFY, EmbeddedDocument, EmbeddedDocumentField, DictField)
from datetime import datetime, timezone
from Models.course_model import Course
from Models.year_model import Year
from Models.admin_model import Admin
from Models.university_model import University
from Models.institution_model import Institution
from Models.class_question_bank import ClassQuestionBank


class Doap(Document):
    university = ReferenceField(University, reverse_delete_rule=CASCADE)
    institution = ReferenceField(Institution, reverse_delete_rule=CASCADE)
    course = ReferenceField(Course, reverse_delete_rule=CASCADE)
    year = ReferenceField(Year, reverse_delete_rule=CASCADE)
    # month_year = DateTimeField(required=True)
    created_by = ReferenceField(
        Admin, reverse_delete_rule=NULLIFY, required=True)
    section = StringField()
    created_at = DateTimeField(default=lambda: datetime.now(timezone.utc))
    status = StringField()
    subject = ListField()
    layer1 = ListField()
    layer2 = ListField()
    layer3 = ListField()
    published = BooleanField(default=False)
    evaluation = BooleanField(default=False)
    evaluation_status = StringField(default="Incomplete")
    analytics = BooleanField(default=False)
    analytics_data = DictField()
