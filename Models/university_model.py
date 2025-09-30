from mongoengine import Document, StringField,DictField


class University(Document):
    university_id = StringField(required=True, unique=True)
    name = StringField(required=True)
    country = StringField()
    website_url = StringField()
    type = StringField()
    address = DictField()
    key = StringField(required=True, unique=True)
    icon = StringField()

    def to_json(self):
        return {
            'id': str(self.id),
            'university_id': self.university_id,
            'name': self.name,
            'country': self.country,
            'website_url': self.website_url,
            'type': self.type,
            'address': self.address if self.address else None,
            'key': self.key if self.key else None,
            'icon': self.icon if self.icon else None,
        }