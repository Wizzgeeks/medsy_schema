from mongoengine import  Document, StringField,DateTimeField
from datetime import datetime,timezone


class Admin_Onboard(Document):
    name = StringField(required=True)
    phone_country = StringField(required=True, default="IND")
    country_code = StringField(required=True, default="+91")
    phone = StringField(required=True, unique=True)
    active = StringField(default=True)
    created_at = DateTimeField(default=datetime.now(timezone.utc))