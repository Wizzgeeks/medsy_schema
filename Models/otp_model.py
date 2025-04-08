from mongoengine import  Document, StringField, IntField,DateTimeField
from datetime import datetime,timezone


class OTPModel(Document):
    phone = StringField(required=True, unique=True)
    otp = IntField()
    exp=DateTimeField()