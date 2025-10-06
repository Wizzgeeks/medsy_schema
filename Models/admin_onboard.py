from mongoengine import  Document, StringField,DateTimeField,BooleanField
from datetime import datetime,timezone


class Admin_Onboard(Document):
    name = StringField(required=True)
    phone_country = StringField(required=True, default="IND")
    country_code = StringField(required=True, default="+91")
    phone = StringField(required=True, unique=True)
    active = BooleanField(default=True)
    created_at = DateTimeField(default=datetime.now(timezone.utc))


    def to_json(self):
        return {
            'id': str(self.id),
            'name': self.name,
            'phone_country': self.phone_country if self.phone_country else None,
            'country_code': self.country_code if self.country_code else None,
            'phone': self.phone if self.phone else None,
            'active': self.active if self.active else None,
            'created_at': self.created_at.isoformat() if self.created_at else None,
        }

