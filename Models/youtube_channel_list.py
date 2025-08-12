from mongoengine import Document,ReferenceField,ListField,CASCADE
from Models.course_model import Course
from Models.subject_model import Subject
from Models.year_model import Year

class Channels(Document):
    course = ReferenceField(Course,required=True,reverse_delete_rule=CASCADE)
    subject = ReferenceField(Subject,required=True,reverse_delete_rule=CASCADE)
    year = ReferenceField(Year,reverse_delete_rule=CASCADE)
    channels = ListField()
    

    def to_json(self):
        return {
            "id": str(self.id),
            "course":str(self.course.id) if self.course else None,
            "subject":str(self.subject.id) if self.subject else None,
            "year":str(self.year.id) if self.year else None,
            "channels":self.channels
            
        }
