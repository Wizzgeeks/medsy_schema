from mongoengine import (
    Document, EmbeddedDocument, StringField,
    ReferenceField, ListField, IntField,
    EmbeddedDocumentField, CASCADE,
    BooleanField
)

from Models.doap_model import Doap
from Models.doap_activity_model import DoapActivity
from Models.doap_activity_question_model import DoapActivityQuestion
from Models.user_model import User


# ======================================
# Student Answer Embedded Model
# ======================================

class StudentAnswerItem(EmbeddedDocument):

    question = StringField(required=True)  # copied from template

    student_answer = StringField()

    faculty_remarks = StringField()

    mark = IntField(min_value=0)

    status = StringField(
        choices=("P", "F1", "F2", "F3", "F4"),
        default=None
    )


# ======================================
# Student Attempt Model
# ======================================

class DoapActivityStudent(Document):

    doap_id = ReferenceField(Doap, reverse_delete_rule=CASCADE, required=True)

    doap_activity_id = ReferenceField(
        DoapActivity,
        reverse_delete_rule=CASCADE,
        required=True
    )

    doap_activity_question_id = ReferenceField(
        DoapActivityQuestion,
        reverse_delete_rule=CASCADE,
        required=True
    )

    student_id = ReferenceField(
        User,
        reverse_delete_rule=CASCADE,
        required=True
    )

    attempt_count = IntField(default=1)

    answers = ListField(
        EmbeddedDocumentField(StudentAnswerItem),
        required=True
    )

    overall_status = StringField(
        choices=("P", "F1", "F2", "F3", "F4"),
        default=None
    )

    completed = BooleanField(default=False)
    meta = {"collection": "doap_activity_student"}
