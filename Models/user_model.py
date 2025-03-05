from mongoengine import Document, StringField

class User(Document):
    course =StringField()
    year = StringField()
    username = StringField(required=True)
    # email = EmailField(unique=True,required=False,default=None)
    # phone= StringField(unique=True,required=False,sparse=True)
    profile=StringField()
    role=StringField(choices=['student','admin','superadmin'],required=True)
    auth_token = StringField()
    password=StringField()
    institution=StringField()
    location=StringField()
    specialisation=StringField()
    position=StringField()
    examTarget=StringField()

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
            "course": str(self.course.id) if self.course else None,
            "year": str(self.year.year) if self.year else None,
            "username": self.username,
            # "email": self.email if self.email else None,
            "profile":self.profile if self.profile else None,
            # "phone":self.phone if self.phone else None,
            "role":self.role if self.role else None,
            "institution":self.institution if self.institution else None,
            "location":self.location if self.location else None,
            "examTarget":self.examTarget if self.examTarget else None,
            "specialisation":self.specialisation if self.specialisation else None

        }

    def with_key(self):
        return {
            "id": str(self.id),
            "course": self.course.to_json() if self.course else None,
            "year": self.year.to_json() if self.year else None,
            "username": self.username,
            # "email": self.email if self.year else None,
            "profile":self.profile if self.year else None,
            # "phone":self.phone if self.year else None,
            "role":self.role if self.year else None,
            "institution":self.institution if self.institution else None,
            "location":self.location if self.location else None,
            "examTarget":self.examTarget if self.examTarget else None,
            "specialisation":self.specialisation if self.specialisation else None
        }
