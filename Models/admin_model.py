from mongoengine import Document, StringField,EmailField,ReferenceField,IntField,ListField,DateTimeField,CASCADE

from datetime import datetime,timezone
from Models.institution_model import Institution
from Models.university_model import University
from Models.course_model import Course
from Models.subject_model import Subject

class Admin(Document):
    email=EmailField(required=True,unique=True)
    admin_id = StringField(required=True, unique=True)
    name = StringField(required=True)
    password=StringField(required=True)
    designation = StringField()
    phone = StringField(required=True)
    role = StringField(choices=['admin','superadmin','staff'],required=True)
    permission_roles = ListField(StringField())
    # university = ReferenceField(University,required=True,reverse_delete_rule=CASCADE)
    # institution = ReferenceField(Institution,required=True,reverse_delete_rule=CASCADE)
    course = ListField(ReferenceField(Course))
    subject = ListField(ReferenceField(Subject))
    section = ListField(StringField())
    status = ListField(StringField())
    active = StringField(choices=['Active','Inactive'],default='Active')
    created_at = DateTimeField(default=datetime.now(timezone.utc))
    auth_token=StringField()

    def to_json(self):
        return {
            'id': str(self.id),
            'admin_id': self.admin_id,
            'email': self.email,
            'name': self.name,
            'role': self.role,
            'phone': self.phone,
            'designation': self.designation,
            'permission_roles': self.permission_roles,
            # 'university': str(self.university.id) if self.university else None,
            # 'institution': str(self.institution.id) if self.institution else None,
            'course': [str(c.id) for c in self.course],
            'subject': [str(s.id) for s in self.subject],
            'section': self.section,
            'status': self.status,
            'active': self.active,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'auth_token': self.auth_token
        }
    def remove_expired_tokens(self):
        current_time = datetime.now(timezone.utc)
        valid_tokens = [token for token in self.auth_token if 'exp' in token and token['exp'] > current_time]
        self.update(set__auth_token=valid_tokens if valid_tokens else "")


        