from mongoengine import Document, StringField,DictField,DateTimeField
from datetime import datetime,timezone

class University(Document):
    name = StringField(required=True)
    country = StringField()
    website_url = StringField()
    type = StringField()
    address = DictField()
    key = StringField(required=True, unique=True)
    icon = StringField()
    created_at = DateTimeField(default=datetime.now(timezone.utc))

    def to_json(self):
        return {
            'id': str(self.id),
            'name': self.name,
            'country': self.country,
            'website_url': self.website_url,
            'type': self.type,
            'address': self.address if self.address else None,
            'key': self.key if self.key else None,
            'icon': self.icon if self.icon else None,
            'created_at': self.created_at.isoformat() if self.created_at else None,
        }