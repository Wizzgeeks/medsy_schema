from mongoengine import Document, StringField,EmailField,ReferenceField,CASCADE,ListField,DateTimeField

from datetime import datetime,timezone
from Models.institution_model import Institution
from Models.university_model import University
from Models.course_model import Course
from Models.subject_model import Subject

class Admin(Document):
    email=EmailField(required=True,unique=True)
    name = StringField(required=True)
    password=StringField(required=True)
    role = StringField(choices=['admin','superadmin','staff'],required=True)
    university = ListField(ReferenceField(University, reverse_delete_rule=CASCADE))
    institution = ListField(ReferenceField(Institution, reverse_delete_rule=CASCADE))
    course = ListField(ReferenceField(Course, reverse_delete_rule=CASCADE))
    subject = ListField(ReferenceField(Subject, reverse_delete_rule=CASCADE))
    created_at = DateTimeField(default=datetime.now(timezone.utc))
    auth_token=StringField()

    def to_json(self):
        return {
            'id': str(self.id),
            'email': self.email,
            'name': self.name,
            'role': self.role,
            'university': [str(u.id) for u in self.university],
            'institution': [str(i.id) for i in self.institution],
            'course': [str(c.id) for c in self.course],
            'subject': [str(s.id) for s in self.subject],
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'auth_token': self.auth_token
        }
    def remove_expired_tokens(self):
        current_time = datetime.now(timezone.utc)
        valid_tokens = [token for token in self.auth_token if 'exp' in token and token['exp'] > current_time]
        self.update(set__auth_token=valid_tokens if valid_tokens else "")


        