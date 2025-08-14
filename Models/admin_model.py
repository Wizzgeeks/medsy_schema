from mongoengine import Document, StringField,EmailField,ReferenceField,IntField,ListField,DateTimeField,BooleanField

from datetime import datetime,timezone
from Models.institution_model import Institution
from Models.university_model import University
from Models.course_model import Course
from Models.year_model import Year
from Models.subject_model import Subject

class Admin(Document):
    email=EmailField(required=True,unique=True)
    name = StringField(required=True)
    password=StringField(required=True)
    qualification = StringField()
    designation = StringField()
    experience = StringField()
    phone = IntField()
    role = StringField(choices=['admin','superadmin','staff'],required=True)
    permission_roles = ListField(StringField())
    university = ListField(ReferenceField(University))
    institution = ListField(ReferenceField(Institution))
    course = ListField(ReferenceField(Course))
    year = ListField(ReferenceField(Year))
    subject = ListField(ReferenceField(Subject))
    section = ListField(StringField())
    status = StringField()
    active = BooleanField(default=True)
    created_at = DateTimeField(default=datetime.now(timezone.utc))
    auth_token=StringField()

    def to_json(self):
        return {
            'id': str(self.id),
            'email': self.email,
            'name': self.name,
            'role': self.role,
            'phone': self.phone,
            'qualification': self.qualification,
            'designation': self.designation,
            'experience': self.experience,
            'permission_roles': self.permission_roles,
            'university': [str(u.id) for u in self.university],
            'institution': [str(i.id) for i in self.institution],
            'course': [str(c.id) for c in self.course],
            'year': [str(y.id) for y in self.year],
            'subject': [str(s.id) for s in self.subject],
            'section': self.section,
            'status': self.status,
            'active': self.active,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'auth_token': self.auth_token,
            
        }
    def remove_expired_tokens(self):
        current_time = datetime.now(timezone.utc)
        valid_tokens = [token for token in self.auth_token if 'exp' in token and token['exp'] > current_time]
        self.update(set__auth_token=valid_tokens if valid_tokens else "")


        