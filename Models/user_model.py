from mongoengine import Document, StringField,BooleanField,ListField,IntField,DateTimeField,ReferenceField,CASCADE
from datetime import datetime,timezone
from Models.institution_model import Institution
from Models.university_model import University

class User(Document):
    university = ReferenceField(University,required=True, reverse_delete_rule=CASCADE)
    institution = ReferenceField(Institution,required=True, reverse_delete_rule=CASCADE)
    course =StringField()
    year = StringField()
    username = StringField(required=True)
    profile=StringField()
    role=StringField(choices=['student','admin','superadmin'],required=True)
    auth_token = StringField()
    password=StringField()
    institution=StringField()
    location=StringField()
    specialisation=StringField()
    position=StringField()
    examTarget=StringField()
    newuser=BooleanField(default=True,required=True)
    referral_code=StringField(required=True,unique=True)
    refered_by=StringField()
    refered_users=ListField(default=[])
    coins = IntField(default=0)
    created_at=DateTimeField(default=datetime.now(timezone.utc))

    def update(self, **kwargs):
        self.clean()
        return super().update(**kwargs)
    # def clean(self):
    #     if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', self.email):
    #         raise ValueError("Enter a Valid mail")
    #     if self.role == 'user':
    #         if not self.course:
    #             raise ValueError("Please select a course")
    def to_json(self):
        return {
            "id": str(self.id),
            "university":str(self.university.id) if self.university else None,
            "institution":str(self.institution.id) if self.institution else None,
            "course": (self.course) if self.course else None,
            "year": (self.year) if self.year else None,
            "username": self.username,
            "profile":self.profile if self.profile else None,
            "role":self.role if self.role else None,
            "institution":self.institution if self.institution else None,
            "position":self.position if self.position else None,
            "location":self.location if self.location else None,
            "examTarget":self.examTarget if self.examTarget else None,
            "specialisation":self.specialisation if self.specialisation else None,
            "newuser":self.newuser if self.newuser else None,
            "referral_code":self.referral_code if self.referral_code else None,
            "refered_by":self.refered_by if self.refered_by else None,
            "refered_users":self.refered_users if self.refered_users else None,
            "coins":self.coins if self.coins else 0,
            'created_at':str(self.created_at) if self.created_at else None,
        }

    def with_key(self):
        return {
            "id": str(self.id),
            "university":str(self.university.id) if self.university else None,
            "institution":str(self.institution.id) if self.institution else None,
            "course": self.course if self.course else None,
            "year": self.year if self.year else None,
            "username": self.username,
            "profile":self.profile if self.year else None,
            "role":self.role if self.year else None,
            "institution":self.institution if self.institution else None,
            "location":self.location if self.location else None,
            "examTarget":self.examTarget if self.examTarget else None,
            "specialisation":self.specialisation if self.specialisation else None,
            "position":self.position if self.position else None,
            "newuser":self.newuser if self.newuser else None,
            "referral_code":self.referral_code if self.referral_code else None,
            "refered_by":self.refered_by if self.refered_by else None,
            "refered_users":self.refered_users if self.refered_users else None,
            "coins":self.coins if self.coins else 0,
            'created_at':str(self.created_at) if self.created_at else None,
        }
    def remove_expired_tokens(self):
        current_time = datetime.now(timezone.utc)
        valid_tokens = [token for token in self.authToken if 'exp' in token and token['exp'] > current_time]
        self.update(set__authToken=valid_tokens if valid_tokens else "")
