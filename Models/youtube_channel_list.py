from mongoengine import Document,ReferenceField,ListField
from Models.course_model import Course
from Models.subject_model import Subject
from Models.year_model import Year

class Layer_3(Document):
    course = ReferenceField(Course,required=True,reverse_delete_rule=2)
    subject = ReferenceField(Subject,required=True,reverse_delete_rule=2)
    year = ReferenceField(Year,reverse_delete_rule=2)
    channels = ListField()
    

    def to_json(self):
        return {
            "id": str(self.id),
            "course":str(self.course.id) if self.course else None,
            "subject":str(self.subject.id) if self.subject else None,
            "year":str(self.year.id) if self.year else None,
            "channels":self.channels
            
        }
