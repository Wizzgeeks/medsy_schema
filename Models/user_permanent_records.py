from mongoengine import Document,DateTimeField,StringField
from datetime import datetime,timezone


class UserRecords(Document):
    email = StringField()
    phone_country = StringField()
    country_code = StringField()
    phone_no = StringField()
    created_at = DateTimeField(default=datetime.now(timezone.utc))
    
    def to_json(self):
        return {
            "id": str(self.id),
            "email":self.email if self.email else None,
            "phone_country":self.phone_country if self.phone_country else None,
            "country_code":self.country_code if self.country_code else None,
            "phone_no":self.phone_no if self.phone_no else None,
            'created_at':str(self.created_at) if self.created_at else None,
        }
