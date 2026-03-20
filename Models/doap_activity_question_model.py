from mongoengine import (
    Document, EmbeddedDocument, StringField,
    ReferenceField, ListField, EmbeddedDocumentField, CASCADE
)
from Models.doap_activity_model import DoapActivity
from Models.doap_model import Doap

# ================================
# Embedded Question Model (TEMPLATE ONLY)
# ================================


class QuestionItem(EmbeddedDocument):
    text = StringField(required=True)


# ================================
# Main Doap Activity Question Model (TEMPLATE)
# ================================

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

    main_description = StringField(required=True)

    images = ListField(
        StringField(),
        max_length=4
    )

    # Only question text stored here
    questions = ListField(
        EmbeddedDocumentField(QuestionItem),
        required=True
    )

    meta = {"collection": "doap_activity_questions"}
