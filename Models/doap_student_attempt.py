from mongoengine import (
    Document, ReferenceField, ListField,
    StringField, BooleanField, IntField,
    DateTimeField, EmbeddedDocumentField, CASCADE
)
from datetime import datetime, timezone
from Models.doap_activity_student_model import StudentAnswerItem
from Models.doap_activity_student_model import DoapActivityStudent
from Models.doap_activity_student_model import StudentAnswerItem

class DoapActivityAttempt(Document):
    """
    Stores the actual submitted answers for one student attempt.
    assignment_id → DoapActivityStudent (the assignment record).
    """

    assignment_id = ReferenceField(
        DoapActivityStudent,
        required=True,
        reverse_delete_rule=CASCADE
    )
    attempt_count  = IntField(default=1)
    answers = ListField(
        EmbeddedDocumentField(StudentAnswerItem),
        required=True
    )
    overall_status = StringField()
    completed      = BooleanField(default=False)

    created_at = DateTimeField(default=lambda: datetime.now(timezone.utc))

    meta = {
        "collection": "doap_student_attempt",
        "indexes": [
            "assignment_id",
            {"fields": ["assignment_id", "attempt_count"]}
        ]
    }
