from mongoengine import Document, StringField,EmailField,ReferenceField,BooleanField,ListField,DateTimeField,CASCADE

from datetime import datetime,timezone
from Models.institution_model import Institution
from Models.university_model import University
# from Models.course_model import Course
# from Models.year_model import Year
# from Models.subject_model import Subject

class Admin(Document):
    email=EmailField(required=True,unique=True)
    admin_id = StringField(required=True)
    name = StringField(required=True)
    password=StringField(required=True)
    designation = StringField()
    country_code = StringField(required=True,default="+91")
    phone_country = StringField(required=True,default="IND")
    phone = StringField(required=True,unique=True)
    role = StringField(choices=['admin','superadmin','staff'],required=True)
    permission_roles = ListField(StringField())
    university = ReferenceField(University,reverse_delete_rule=CASCADE)
    institution = ReferenceField(Institution,reverse_delete_rule=CASCADE)
    course = ListField(StringField())
    # department = ListField(StringField())
    year = ListField(StringField())
    subject = ListField(StringField())
    section = ListField(StringField())
    status = ListField(StringField())
    active = StringField(choices=['Active','Inactive'],default='Active')
    created_at = DateTimeField(default=datetime.now(timezone.utc))
    auth_token=StringField()
    new_staff = BooleanField(default=False)

    def to_json(self):
        return {
            'id': str(self.id),
            'admin_id': self.admin_id,
            'email': self.email,
            'name': self.name,
            'role': self.role,
            'country_code': self.country_code if self.country_code else "+91",
            'phone_country': self.phone_country if self.phone_country else "IND",
            'phone': self.phone,
            'designation': self.designation,
            'permission_roles': self.permission_roles,
            'university': str(self.university.id) if self.university else None,
            'institution': str(self.institution.id) if self.institution else None,
            # 'department': self.department,
            'course': self.course,
            'year': self.year,
            'subject': self.subject,
            'section': self.section,
            'status': self.status,
            'active': self.active,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'new_staff': self.new_staff,
            'auth_token': self.auth_token
        }
    

    def with_json(self):
        return {
            'id': str(self.id),
            'admin_id': self.admin_id,
            'email': self.email,
            'name': self.name,
            'role': self.role,
            'country_code': self.country_code if self.country_code else "+91",
            'phone_country': self.phone_country if self.phone_country else "IND",
            'phone': self.phone,
            'designation': self.designation,
            'permission_roles': self.permission_roles,
            'university': {"id": str(self.university.id), "name": self.university.name} if self.university else None,
            'institution': {"id": str(self.institution.id), "name": self.institution.name} if self.institution else None,
            # 'department': self.department,
            'course': self.course,
            'year': self.year,
            'subject': self.subject,
            'section': self.section,
            'status': self.status,
            'active': self.active,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'new_staff': self.new_staff,
            'auth_token': self.auth_token
        }

    def remove_expired_tokens(self):
        current_time = datetime.now(timezone.utc)
        valid_tokens = [token for token in self.auth_token if 'exp' in token and token['exp'] > current_time]
        self.update(set__auth_token=valid_tokens if valid_tokens else "")


        