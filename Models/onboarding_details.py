from mongoengine import Document, StringField,DateTimeField, ReferenceField,CASCADE
from datetime import datetime,timezone
from Models.university_model import University
from Models.institution_model import Institution

class Onboard_details(Document):
    type = StringField()
    university = ReferenceField(University, required=True, reverse_delete_rule=CASCADE)
    institution = ReferenceField(Institution, required=True, reverse_delete_rule=CASCADE)
    domain = StringField()
    phone_country = StringField(required=True, default="India")
    country_code = StringField(required=True, default="+91")
    phone = StringField(required=True)
    email = StringField(required=True)
    phone_country_optional = StringField()
    country_code_optional = StringField()
    phone_optional = StringField()
    email_optional = StringField()
    created_at = DateTimeField(default=datetime.now(timezone.utc))

    def to_json(self):
        return {
            'id': str(self.id),
            'type': self.type,
            'university_id': str(self.university.id) if self.university else None,
            'institution_id': str(self.institution.id) if self.institution else None,
            'domain': self.domain if self.domain else None,
            'phone_country': self.phone_country if self.phone_country else None,
            'country_code': self.country_code if self.country_code else None,
            'phone': self.phone if self.phone else None,
            'email': self.email if self.email else None,
            'country_code_optional': self.country_code_optional if self.country_code_optional else None,
            'phone_country_optional': self.phone_country_optional if self.phone_country_optional else None,
            'phone_optional': self.phone_optional if self.phone_optional else None,
            'email_optional': self.email_optional if self.email_optional else None,
            'created_at': self.created_at.isoformat() if self.created_at else None,
        }