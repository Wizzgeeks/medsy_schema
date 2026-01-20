from mongoengine import Document,ReferenceField,BooleanField,ListField,CASCADE
from Models.user_model import User
from Models.course_model import Course
from Models.year_model import Year
from Models.subject_model import Subject


class Completed(Document):
    
    course = ReferenceField(Course,reverse_delete_rule=CASCADE,required=True)
    year = ReferenceField(Year,reverse_delete_rule=CASCADE,required=True)
    subject=ListField()
    layer1 = ListField()
    layer2 = ListField()
    layer3 = ListField()
    user = ReferenceField(User,reverse_delete_rule=CASCADE,required=True)
    completed=BooleanField(default=False)


    def to_json(self):
        return {
            "course":str(self.course.id),
            "year":str(self.year.id),
            "layer1":self.layer1 if self.layer1 else None,
            "layer2":self.layer2 if self.layer2 else None,
            "layer3":self.layer3 if self.layer3 else None,
            "user":str(self.user.id) if self.user else None,
            "completed":self.completed
        }