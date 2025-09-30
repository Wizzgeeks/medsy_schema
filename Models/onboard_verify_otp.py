from mongoengine import  Document, StringField, IntField,DateTimeField


class OnboardVerifyOTP(Document):
    phone = StringField(required=True, unique=True)
    otp = IntField()
    exp = DateTimeField()