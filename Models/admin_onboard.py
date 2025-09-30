from mongoengine import  Document, StringField,DateTimeField
from datetime import datetime,timezone


class Admin_Onboard(Document):
    name = StringField(required=True)
    phone = StringField(required=True, unique=True)
    active = StringField(default=True)
    created_at = DateTimeField(default=datetime.now(timezone.utc))