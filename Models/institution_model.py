from mongoengine import Document, StringField, DictField, ReferenceField,CASCADE,DateTimeField
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
    created_at = DateTimeField(default=datetime.now(timezone.utc))



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
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'phone_country': self.phone_country if self.phone_country else None,
            'country_code': self.country_code if self.country_code else None,
            'phone': self.phone if self.phone else None,
            'email': self.email if self.email else None,
            
        }
