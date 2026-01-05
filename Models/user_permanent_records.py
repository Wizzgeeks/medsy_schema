from mongoengine import Document, DateTimeField, StringField
from datetime import datetime, timezone

class UserRecords(Document):
    email_hash = StringField(unique=True, sparse=True)
    phone_hash = StringField(unique=True, sparse=True)

    country_code = StringField()
    created_at = DateTimeField(default=datetime.now(timezone.utc))

    meta = {
        "collection": "user_records",
        "indexes": ["email_hash", "phone_hash"]
    }
