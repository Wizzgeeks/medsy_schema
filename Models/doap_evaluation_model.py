from mongoengine import (
    Document, ReferenceField, ListField,
    DictField, FloatField, StringField,
    BooleanField, DateTimeField, CASCADE, NULLIFY
)
from datetime import datetime, timezone
from Models.doap_activity_model import DoapActivity
from Models.user_model import User
from Models.admin_model import Admin

class DoapEvaluation(Document):
    """Faculty evaluation of a student's submitted attempt."""
 doap_activity_id = ReferenceField(DoapActivity, required=True, reverse_delete_rule=CASCADE)
    student_id = ReferenceField(User, required=True, reverse_delete_rule=CASCADE)

    # DoapActivityStudent ObjectId as string (works for all activity types)
    attempt_id    = StringField(required=True)
    activity_type = StringField(required=True,
                                choices=("OSPE", "OSCE", "Interpretation", "Image"))

       evaluated_by = ReferenceField(Admin, reverse_delete_rule=NULLIFY)

    # Per-item evaluation dicts
    # Checklist:  {sequence, item_text, is_correct, mark, remarks}
    checklist_evaluations  = ListField(DictField(), default=[])
    # Form:       {sequence, item_text, student_answer, is_correct, mark, remarks}
    form_evaluations       = ListField(DictField(), default=[])
    # Scaffolded: {sequence, question_text, question_type, student_answer,
    #              is_correct, mark, remarks}
    scaffolded_evaluations = ListField(DictField(), default=[])

    obtained_marks   = FloatField(default=0)
    overall_remarks  = StringField()
    faculty_decision = StringField(choices=("C", "R", "Re"))   # Completed/Repeat/Remedial
    rating           = StringField(choices=("M", "E", "B"))    # Meets/Exceeds/Below

    eval_status  = StringField(choices=("incomplete", "completed"), default="incomplete")
    evaluated_at = DateTimeField()

    meta = {
        "collection": "doap_evaluation",
        "indexes": [
            {"fields": ["doap_activity_id", "student_id", "attempt_id"], "unique": True}
        ]
    }
