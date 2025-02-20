from mongoengine import Document, ReferenceField, StringField,EmailField
from Models.course_model import Course
from Models.year_model import Year
import re

class User(Document):
    course = ReferenceField(Course, required=True, reverse_delete_rule=2)
    year = ReferenceField(Year, reverse_delete_rule=2)
    username = StringField(required=True)
    email = EmailField(unique=True,default=None)
    phone= StringField(unique=True,default=None)
    profile=StringField()
    role=StringField()
    auth_token = StringField()
    password=StringField()

    def clean(self):
        if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', self.email):
            raise ValueError("Enter a Valid mail")


    def to_json(self):
        return {
            "id": str(self.id),
            "course": str(self.course.id) if self.course else None,
            "year": str(self.year.id) if self.year else None,
            "username": self.username,
            "email": self.email if self.year else None,
            "profile":self.profile if self.year else None,
            "phone":self.phone if self.year else None,
            "role":self.role if self.year else None

        }

    def with_key(self):
        return {
            "id": str(self.id),
            "course": self.course.to_json() if self.course else None,
            "year": self.year.to_json() if self.year else None,
            "username": self.username,
            "email": self.email if self.year else None,
            "profile":self.profile if self.year else None,
            "phone":self.phone if self.year else None,
            "role":self.role if self.year else None
        }
    
    def update(self, **kwargs):
        self.clean()
        return super().update(**kwargs)

