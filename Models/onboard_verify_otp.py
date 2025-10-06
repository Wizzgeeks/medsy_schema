from mongoengine import  Document, StringField, IntField,DateTimeField


class OnboardVerifyOTP(Document):
    country_code = StringField(default="+91")
    phone = StringField(required=True, unique=True)
    otp = IntField()
    exp = DateTimeField()