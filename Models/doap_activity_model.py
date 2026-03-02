from mongoengine import (
    Document, StringField, ReferenceField,
    BooleanField, CASCADE,
    DateTimeField
)
from Models.doap_model import Doap


class DoapActivity(Document):
    doap_id = ReferenceField(Doap, reverse_delete_rule=CASCADE)

    name = StringField(required=True)

    type = StringField(
        required=True,
        choices=("OSPE", "OSCE", "Interpretation", "Image")
    )

    status = StringField(
        choices=("Generated", "Created"),
        default=None
    )

    assignyear = StringField()  # example: "2024", "1st Year"

    assigned_section = StringField()  # example: "A", "B", "C"

    enable_marks = BooleanField(default=False)

    is_assigned = BooleanField(default=False)

    assigned_date = DateTimeField()

    meta = {"collection": "doap_activity"}

    def clean(self):
        # Auto-set status based on type
        if self.type in ("Interpretation", "Image"):
            self.status = "Created"
        elif self.type in ("OSPE", "OSCE"):
            self.status = "Generated"
