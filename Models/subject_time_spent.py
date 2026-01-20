from mongoengine import Document,ReferenceField,IntField,DictField,ListField,StringField,BooleanField,CASCADE
from Models.user_model import User
from Models.course_model import Course
from Models.subject_model import Subject
from Models.year_model import Year
from Models.subject_page_model import Subject_page
class Subject_time_spent(Document):
    course = ReferenceField(Course,reverse_delete_rule=CASCADE,required=True)
    subject = ReferenceField(Subject,reverse_delete_rule=CASCADE,required=True)
    year = ReferenceField(Year,reverse_delete_rule=CASCADE,required=True)
    user = ReferenceField(User,reverse_delete_rule=CASCADE,required=True)
    subject_page = ReferenceField(Subject_page,reverse_delete_rule=CASCADE,required=True)
    attempts =ListField(DictField())
    types=StringField(choices=['mcq','test_series','ctc_fillups','ctc_mcq','ctc_analysis','content','exam'],required=True)
    completed=BooleanField(default=False)
    child=BooleanField(default=False) 
    parent=BooleanField(default=False)
    


    def to_json(self):
        return {
            # "layer1":str(self.layer1.id) if self.layer1 else None,
            # "user":str(self.user.id) if self.user else None,
            # "course":str(self.course.id) if self.course else None,
            # "subject":str(self.subject.id) if self.subject else None,
            "user":self.user.to_json() if self.user else None,
            "course":self.course.to_json() if self.course else None,
            "subject":self.subject.to_json() if self.subject else None,
            "year":self.year.to_json() if self.year else None,
            "subject_page":self.subject_page.to_json() if self.subject_page else None,
            "attempts":self.attempts,
            "types":self.types,
            "completed":self.completed,
            "child": self.child,
            "parent": self.parent
            }