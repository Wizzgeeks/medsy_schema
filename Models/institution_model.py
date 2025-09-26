from mongoengine import Document, StringField, IntField, DictField, ReferenceField,CASCADE
from Models.university_model import University

class Institution(Document):
    institution_id = StringField(required=True, unique=True)
    name = StringField(required=True, unique=True)
    abbreviation = StringField()
    code = StringField()
    established_year = IntField()
    type = StringField()
    address = DictField()
    university = ReferenceField(University,required=True, reverse_delete_rule=CASCADE)
    key = StringField(required=True, unique=True)
    icon = StringField()
    cover_image = StringField()
    about_us = StringField()


    def to_json(self):
        return {
            'id': str(self.id),
            'institution_id': self.institution_id,
            'name': self.name,
            'abbreviation': self.abbreviation,
            'established_year': self.established_year,
            'type': self.type,
            'code': self.code,
            'address': self.address if self.address else None,
            'university_id': str(self.university.id) if self.university else None,
            'key': self.key if self.key else None,
            'icon': self.icon if self.icon else None,
            'cover_image': self.cover_image if self.cover_image else None,
            'about_us': self.about_us if self.about_us else None,
        }
