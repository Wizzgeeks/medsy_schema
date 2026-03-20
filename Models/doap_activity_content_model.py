from mongoengine import (
    Document, ReferenceField, ListField,
    DictField, StringField, DateTimeField,
    CASCADE
)
from datetime import datetime, timezone
from Models.doap_model import Doap
# Remove this direct import - it's causing circular import
# from Models.doap_activity_model import DoapActivity

class DoapActivityContent(Document):
    """
    AI-generated content for OSPE/OSCE activities.
    Also used (partially) for Interpretation/Image scaffolded question generation.
    Never modified after generation — edits go to DoapActivityContentOverride.
    """

    doap_id = ReferenceField(Doap, reverse_delete_rule=CASCADE, required=True)

    # Use string reference instead of direct import
    doap_activity_id = ReferenceField(
        'DoapActivity', reverse_delete_rule=CASCADE, required=True  # Changed to string
    )
    activity_name    = StringField()
    doap_type        = StringField()   # "OSPE" | "OSCE" | "Interpretation" | "Image"

    # "Pending" | "Generating" | "Done" | "Failed"
    generation_status = StringField(default="Pending")
    error_message     = StringField()

    # Generated content (list of dicts matching checklist/form/question schema)
    faculty_checklist      = ListField(DictField(), default=[])
    student_activity_form  = ListField(DictField(), default=[])
    scaffolded_questions   = ListField(DictField(), default=[])

    # Optional: question types requested for generation
    selected_question_types = ListField(StringField(), default=[])

    generated_at = DateTimeField()

    meta = {
        "collection": "doap_activity_content",
        "indexes": ["doap_activity_id", "generation_status"]
    }
