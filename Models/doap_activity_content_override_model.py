from mongoengine import (
    Document, ReferenceField, ListField,
    DictField, DateTimeField, CASCADE, NULLIFY
)
from datetime import datetime, timezone
from Models.doap_model import Doap
from Models.doap_activity_model import DoapActivity
from Models.doap_activity_content_model import DoapActivityContent
from Models.institution_model import Institution
from Models.admin_model import Admin

class DoapActivityContentOverride(Document):
    """
    Staff-edited version of DoapActivityContent.
    Original AI content is never modified; overrides live here.
    One override per (activity, staff member) pair.
    """

    doap_activity_id = ReferenceField(
        DoapActivity, reverse_delete_rule=CASCADE, required=True
    )

    doap_id = ReferenceField(Doap, reverse_delete_rule=CASCADE, required=True)

    institution_id = ReferenceField(Institution, reverse_delete_rule=CASCADE, required=True)

    source_content_id = ReferenceField(DoapActivityContent, reverse_delete_rule=NULLIFY)

    # Edited content (mirrors DoapActivityContent structure)
    faculty_checklist     = ListField(DictField(), default=[])
    student_activity_form = ListField(DictField(), default=[])
    scaffolded_questions  = ListField(DictField(), default=[])

    edited_by = ReferenceField(Admin, reverse_delete_rule=NULLIFY)
    edited_at = DateTimeField()

    meta = {
        "collection": "doap_activity_content_override",
        "indexes": [
            {"fields": ["doap_activity_id", "edited_by"]}
        ]
    }
