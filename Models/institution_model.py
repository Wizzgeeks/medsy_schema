from mongoengine import Document, StringField, DictField, ReferenceField,CASCADE,DateTimeField,BooleanField
from datetime import datetime,timezone
from Models.university_model import University

class Institution(Document):
    university = ReferenceField(University,required=True, reverse_delete_rule=CASCADE)
    name = StringField(required=True, unique=True)
    code = StringField()
    type = StringField()
    address = DictField()
    key = StringField(required=True, unique=True)
    icon = StringField()
    cover_image = StringField()
    about_us = StringField()
    website_url = StringField()
    phone_country = StringField(default="IND")
    country_code = StringField(default="+91")
    phone = StringField()
    email = StringField()
    phone_country1 = StringField(default="IND")
    country_code1 = StringField(default="+91")
    phone1 = StringField()
    email1 = StringField()
    phone_country2 = StringField(default="IND")
    country_code2 = StringField(default="+91")
    phone2 = StringField()
    email2 = StringField()
    onboarded = BooleanField(default=False)
    created_at = DateTimeField(default=datetime.now(timezone.utc))
    onboarded_at = DateTimeField()



    def to_json(self):
        return {
            'id': str(self.id),
            'name': self.name,
            'type': self.type,
            'code': self.code,
            'address': self.address if self.address else None,
            'university_id': str(self.university.id) if self.university else None,
            'key': self.key if self.key else None,
            'icon': self.icon if self.icon else None,
            'cover_image': self.cover_image if self.cover_image else None,
            'about_us': self.about_us if self.about_us else None,
            'website_url': self.website_url,
            'created_at': self.created_at.strftime('%d/%m/%Y') if self.created_at else None,
            'phone_country': self.phone_country if self.phone_country else None,
            'country_code': self.country_code if self.country_code else None,
            'phone': self.phone if self.phone else None,
            'email': self.email if self.email else None,
            'phone_country1': self.phone_country1 if self.phone_country1 else None,
            'country_code1': self.country_code1 if self.country_code1 else None,
            'phone1': self.phone1 if self.phone1 else None,
            'email1': self.email1 if self.email1 else None,
            'phone_country2': self.phone_country2 if self.phone_country2 else None,
            'country_code2': self.country_code2 if self.country_code2 else None,
            'phone2': self.phone2 if self.phone2 else None, 
            'email2': self.email2 if self.email2 else None,
            'onboarded': self.onboarded if self.onboarded else False,
            'onboarded_at': self.onboarded_at.strftime('%d/%m/%Y') if self.onboarded_at else None,

        }
