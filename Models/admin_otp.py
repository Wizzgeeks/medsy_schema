from mongoengine import  Document, StringField, IntField,DateTimeField
# from datetime import datetime,timezone


class Admin_Otp(Document):
    phone = StringField(required=True, unique=True)
    otp = IntField()
    exp=DateTimeField()