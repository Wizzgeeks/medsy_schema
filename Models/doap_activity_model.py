from mongoengine import (
    Document, ReferenceField, StringField,
    BooleanField, DateTimeField, CASCADE, NULLIFY
)
from Models.doap_model import Doap
from Models.layer_3_model import Layer_3
# Remove this import
# from Models.doap_activity_content_model import DoapActivityContent

class DoapActivity(Document):

    doap_id     = ReferenceField(Doap, required=True, reverse_delete_rule=CASCADE)
    name        = StringField(required=True)
    type        = StringField(required=True,
                              choices=("OSPE", "OSCE", "Interpretation", "Image"))

    # Link to Layer_3 for competency context (used in AI generation & evaluation)
    layer3_id   = ReferenceField(Layer_3, reverse_delete_rule=NULLIFY)

    # AI-generated content reference (OSPE/OSCE only)
    # Use string reference here too
    content_id  = ReferenceField('DoapActivityContent')  # Changed to string

    is_certified    = BooleanField(default=False)
    is_assigned     = BooleanField(default=False)
    enable_marks    = BooleanField(default=False)

    # "Created" | "Generated" | "Assigned"
    status          = StringField()

    # Which sections are shown to students
    assign_checklist = BooleanField(default=False)
    assign_form      = BooleanField(default=False)
    assign_questions = BooleanField(default=False)

    assigned_date    = DateTimeField()
    # Year key string (e.g. "MB1-FI1") stored at assignment time
    assignyear       = StringField()
    assigned_section = StringField()

    meta = {
        "collection": "doap_activity",
        "indexes": ["doap_id", "type"]
    }
