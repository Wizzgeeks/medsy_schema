from mongoengine import Document,ReferenceField,IntField,ListField,CASCADE
from Models.user_model import User
from Models.course_model import Course
from Models.year_model import Year
from Models.subject_model import Subject


class Time_spent(Document):  
    course = ReferenceField(Course,required=True,reverse_delete_rule=CASCADE)
    year = ReferenceField(Year,required=True,reverse_delete_rule=CASCADE)
    subject=ReferenceField(Subject,required=True,reverse_delete_rule=CASCADE)
    layer1 = ListField()
    layer2 = ListField()
    layer3 = ListField()
    user = ReferenceField(User,required=True,reverse_delete_rule=CASCADE)
    total_time=IntField(required=True)


    def to_json(self):
        return {
            "course":str(self.course.id),
            "year":str(self.year.id),
            "subject":str(self.subject.id) if self.subject else None,
            "layer1":self.layer1 if self.layer1 else None,
            "layer2":self.layer2 if self.layer2 else None,
            "layer3":self.layer3 if self.layer3 else None,
            "user":str(self.user.id) if self.user else None,
            "total_time":self.total_time
        }