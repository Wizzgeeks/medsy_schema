from mongoengine import Document,ReferenceField,BooleanField,CASCADE,IntField
from Models.user_model import User
from Models.course_model import Course
from Models.year_model import Year


class Year_completion_status(Document):
    course=ReferenceField(Course,required=True,reverse_delete_rule=CASCADE)
    year=ReferenceField(Year,required=True,reverse_delete_rule=CASCADE)
    user = ReferenceField(User,required=True,reverse_delete_rule=CASCADE)
    completed=BooleanField(default=False)
    total_time_taken_subject=IntField()
    total_subject_count=IntField()
    completed_subject_count=IntField()


    def to_json(self):
        return {
            "id":str(self.id),
            "course":str(self.course.id) if self.course else None,
            "year":str(self.year.id) if self.year else None,
            "user":str(self.user.id) if self.user else None,
            "completed":self.completed,
            "total_time_taken_subject":self.total_time_taken_subject,
            "total_subject_count":self.total_subject_count,
            "completed_subject_count":self.completed_subject_count
            }

    
    def with_key(self):
        return {
            "id":str(self.id),
            "coures":self.course.to_json() if self.course else None,
            "year":self.year.to_json() if self.year else None,
            "user":str(self.user.id)if self.user else None,
            "completed":self.completed,
            "total_time_taken_subject":self.total_time_taken_subject,
            "total_subject_count":self.total_subject_count,
            "completed_subject_count":self.completed_subject_count
            
        }