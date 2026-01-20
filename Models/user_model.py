from mongoengine import Document, StringField,BooleanField,ListField,IntField,DateTimeField,ReferenceField,CASCADE
from datetime import datetime,timezone
from Models.institution_model import Institution
from Models.university_model import University
from Models.course_model import Course
from Models.year_model import Year


class User(Document):
    university_id = ListField(ReferenceField(University, reverse_delete_rule=CASCADE,required=True))
    institution_id = ListField(ReferenceField(Institution, reverse_delete_rule=CASCADE,required=True))
    course_id = ReferenceField(Course, reverse_delete_rule=CASCADE,required=True)
    year_id = ReferenceField(Year, reverse_delete_rule=CASCADE,required=True)
    user_id = StringField(required=True)
    university = ListField(StringField(required=True))
    institutions = ListField(StringField(required=True))
    course =StringField(required=True)
    year = StringField(required=True)
    section = StringField()
    username = StringField(required=True)
    profile=StringField()
    role=StringField(choices=['student','staff','superadmin'],required=True)
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
    
    def to_json(self):
        return {
            "id": str(self.id),
            "university_id": [str(univer_id.id) for univer_id in self.university_id] if self.university_id else [],
            "institution_id": [str(insti_id.id) for insti_id in self.institution_id] if self.institution_id else [],
            "course_id": str(self.course_id.id) if self.course_id else None,
            "year_id": str(self.year_id.id) if self.year_id else None,
            "user_id": self.user_id if self.user_id else None,
            "university": self.university if self.university else [],
            "institutions": self.institutions if self.institutions else [],
            "section":self.section if self.section else None,
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
            "university_id": [str(univer_id.id) for univer_id in self.university_id] if self.university_id else [],
            "institution_id": [str(insti_id.id) for insti_id in self.institution_id] if self.institution_id else [],
            "course_id": str(self.course_id.id) if self.course_id else None,
            "year_id": str(self.year_id.id) if self.year_id else None,
            "user_id": self.user_id if self.user_id else None,
            "university": self.university if self.university else [],
            "institutions": self.institutions if self.institutions else [],
            "section": self.section if self.section else None,
            "course": (self.course) if self.course else None,
            "year": (self.year) if self.year else None,
            "username": self.username,
            "profile":self.profile if self.profile else None,
            "role":self.role if self.role else None,
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
    
    def admin_get(self):
        return {
            "id": str(self.id),
            "university_id": [{"id":str(uni_id.id),"name":uni_id.name,"key":uni_id.key} for uni_id in self.university_id] if self.university_id else [],
            "institution_id": [{"id":str(insti_id.id),"name":insti_id.name,"key":insti_id.key} for insti_id in self.institution_id] if self.institution_id else [],
            "role":self.role if self.role else None,
            "course_id": str(self.course_id.id) if self.course_id else None,
            "year_id": str(self.year_id.id) if self.year_id else None,
            "course_name": self.course_id.name if self.course_id else None,
            "year_name": self.year_id.year if self.year_id else None,
            "user_id": self.user_id if self.user_id else None,
            "profile":self.profile if self.profile else None,
            "course": (self.course) if self.course else None,
            "year": (self.year) if self.year else None,
            "section": self.section if self.section else None,
            "username": self.username,
            'created_at':str(self.created_at) if self.created_at else None,
        }
    def remove_expired_tokens(self):
        current_time = datetime.now(timezone.utc)
        valid_tokens = [token for token in self.authToken if 'exp' in token and token['exp'] > current_time]
        self.update(set__authToken=valid_tokens if valid_tokens else "")
