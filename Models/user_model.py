from mongoengine import Document, StringField,EmailField,BooleanField,ListField
from datetime import datetime,timezone
class User(Document):
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
    referral_code=StringField(unique=True)
    refered_by=StringField()
    refered_users=ListField()

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
        }

    def with_key(self):
        return {
            "id": str(self.id),
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

        }
    def remove_expired_tokens(self):
        current_time = datetime.now(timezone.utc)
        valid_tokens = [token for token in self.authToken if 'exp' in token and token['exp'] > current_time]
        self.update(set__authToken=valid_tokens if valid_tokens else "")
