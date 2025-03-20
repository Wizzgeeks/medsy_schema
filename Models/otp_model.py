from mongoengine import  Document, StringField, IntField


class OTPModel(Document):
    phone = StringField(required=True, unique=True)
    otp = IntField()