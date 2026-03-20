from mongoengine import (
    Document, ReferenceField, ListField,
    DictField, DateTimeField, CASCADE, NULLIFY
)
from datetime import datetime, timezone


class DoapActivityContentOverride(Document):
    """
    Staff-edited version of DoapActivityContent.
    Original AI content is never modified; overrides live here.
    One override per (activity, staff member) pair.
    """

    doap_activity_id = ReferenceField("DoapActivity", required=True,
                                      reverse_delete_rule=CASCADE)
    doap_id          = ReferenceField("Doap", reverse_delete_rule=CASCADE)
    institution_id   = ReferenceField("Institution", reverse_delete_rule=NULLIFY)
    source_content_id= ReferenceField("DoapActivityContent", reverse_delete_rule=NULLIFY)

    # Edited content (mirrors DoapActivityContent structure)
    faculty_checklist     = ListField(DictField(), default=[])
    student_activity_form = ListField(DictField(), default=[])
    scaffolded_questions  = ListField(DictField(), default=[])

    edited_by = ReferenceField("Admin", reverse_delete_rule=NULLIFY)
    edited_at = DateTimeField()

    meta = {
        "collection": "doap_activity_content_override",
        "indexes": [
            {"fields": ["doap_activity_id", "edited_by"]}
        ]
    }
