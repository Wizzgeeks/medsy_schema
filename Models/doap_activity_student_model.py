from mongoengine import (
    Document, EmbeddedDocument, ReferenceField,
    ListField, StringField, FloatField,
    BooleanField, IntField, DateTimeField,
    EmbeddedDocumentField, CASCADE, NULLIFY
)
from datetime import datetime, timezone


class StudentAnswerItem(EmbeddedDocument):
    """One answer submitted by a student."""
    question       = StringField()
    student_answer = StringField()
    faculty_remarks= StringField()
    mark           = FloatField()
    status         = StringField()


class DoapActivityStudent(Document):
    """Assignment record: one student assigned to one activity attempt."""

    doap_id                 = ReferenceField("Doap", required=True, reverse_delete_rule=CASCADE)
    doap_activity_id        = ReferenceField("DoapActivity", required=True, reverse_delete_rule=CASCADE)
    doap_activity_question_id = ReferenceField("DoapActivityQuestion", reverse_delete_rule=NULLIFY)
    student_id              = ReferenceField("User", required=True, reverse_delete_rule=CASCADE)

    attempt_count   = IntField(default=1)
    answers         = ListField(EmbeddedDocumentField(StudentAnswerItem), default=[])
    overall_status  = StringField()
    completed       = BooleanField(default=False)

    created_at = DateTimeField(default=lambda: datetime.now(timezone.utc))

    meta = {
        "collection": "doap_activity_student",
        "indexes": [
            "student_id",
            "doap_activity_id",
            {"fields": ["doap_id", "doap_activity_id", "student_id"]}
        ]
    }
