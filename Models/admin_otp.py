from mongoengine import  Document, StringField, IntField,DateTimeField
# from datetime import datetime,timezone


class Admin_Otp(Document):
    country_code = StringField(default="+91")
    phone = StringField(required=True, unique=True)
    otp = IntField()
    exp=DateTimeField()