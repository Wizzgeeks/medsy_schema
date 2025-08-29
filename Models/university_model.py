from mongoengine import Document, StringField, IntField,DictField


class University(Document):
    name = StringField(required=True, unique=True)
    established_year = IntField()
    type = StringField()
    address = DictField()
    key = StringField(required=True, unique=True)

    def to_json(self):
        return {
            'id': str(self.id),
            'name': self.name,
            'established_year': self.established_year,
            'type': self.type,
            'address': self.address if self.address else None,
            'key': self.key if self.key else None,
        }