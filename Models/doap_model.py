from mongoengine import (
    Document, ReferenceField, ListField,
    DictField, StringField, CASCADE
)

# Forward-declare to avoid circular imports
class Doap(Document):

    institution   = ReferenceField("Institution")
    university    = ReferenceField("University")
    course        = ReferenceField("Course")
    year          = ReferenceField("Year")
    created_by    = ReferenceField("Admin")

    # Each item: {"name": "...", "clean_name": "..."}
    subject = ListField(DictField(), default=[])
    layer1  = ListField(DictField(), default=[])
    layer2  = ListField(DictField(), default=[])
    # layer3 items also include "id" (layer3 ObjectId) and "competency_key"
    layer3  = ListField(DictField(), default=[])

    meta = {
        "collection": "doap",
        "indexes": [
            {
                "fields": ["institution", "course", "year"],
            }
        ]
    }
