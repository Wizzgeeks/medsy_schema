from mongoengine import (
    Document, EmbeddedDocument, ReferenceField,
    ListField, DictField, StringField,
    FloatField, EmbeddedDocumentField,
    DateTimeField, CASCADE
)
from datetime import datetime, timezone
from Models.doap_activity_model import DoapActivity
from Models.doap_model import Doap

class QuestionItem(EmbeddedDocument):
    """One activity-form question (student fills this in during the activity)."""
    text             = StringField()
    marks            = FloatField()
    cognitive_level  = StringField()
    affective_level  = StringField()
    psychomotor_level= StringField()
    field_type       = StringField()   # "numeric" | "observation" | "calculation"


class DoapActivityQuestion(Document):

   doap_id = ReferenceField(
        Doap,
        reverse_delete_rule=CASCADE,
        required=True
    )

    doap_activity_id = ReferenceField(
        DoapActivity,
        reverse_delete_rule=CASCADE,
        required=True
    )

    main_description = StringField(default="")

    # Activity-form items (student fills during exam)
    questions        = ListField(EmbeddedDocumentField(QuestionItem), default=[])

    # Image URLs (for Image-type activities)
    images           = ListField(StringField(), default=[])

    # Scaffolded questions stored as raw dicts
    # Each dict: {sequence, question_type, question_text, options, correct_answer,
    #             answer_explanation, marks, cognitive_domain, affective_domain,
    #             psychomotor_domain, category}
    scaffolded_questions = ListField(DictField(), default=[])

    created_at = DateTimeField(default=lambda: datetime.now(timezone.utc))
    updated_at = DateTimeField(default=lambda: datetime.now(timezone.utc))

    meta = {
        "collection": "doap_activity_question",
        "indexes": ["doap_id", "doap_activity_id"]
    }
