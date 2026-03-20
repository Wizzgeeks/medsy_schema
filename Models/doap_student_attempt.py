from mongoengine import (
    Document, ReferenceField, ListField,
    EmbeddedDocumentField, IntField,
    BooleanField,
    StringField, CASCADE
)

from Models.doap_activity_student_model import DoapActivityStudent
from Models.doap_activity_student_model import StudentAnswerItem


class DoapActivityAttempt(Document):

    # 🔗 Link to Assignment
    assignment_id = ReferenceField(
        DoapActivityStudent,
        required=True,
        reverse_delete_rule=CASCADE
    )

    # Attempt number (1,2,3...)
    attempt_count = IntField(required=True)

    # Student Answers
    answers = ListField(
        EmbeddedDocumentField(StudentAnswerItem),
        required=True
    )

    overall_status = StringField(
        choices=("P", "F1", "F2", "F3", "F4"),
        default=None
    )
    completed = BooleanField(default=False)

    meta = {"collection": "doap_activity_attempt"}
