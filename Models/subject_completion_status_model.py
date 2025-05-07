from mongoengine import Document,ReferenceField,BooleanField,CASCADE,IntField
from Models.user_model import User
from Models.course_model import Course
from Models.year_model import Year
from Models.subject_model import Subject


class Subject_completion_status(Document):
    course=ReferenceField(Course,required=True,reverse_delete_rule=CASCADE)
    year=ReferenceField(Year,required=True,reverse_delete_rule=CASCADE)
    subject=ReferenceField(Subject,required=True,reverse_delete_rule=CASCADE)
    user = ReferenceField(User,required=True,reverse_delete_rule=CASCADE)
    completed=BooleanField(default=False)
    total_time_taken_pages=IntField()
    total_time_taken_layer=IntField()
    total_page_count=IntField()
    completed_page_count=IntField()
    total_layer_count=IntField()
    completed_layer_count=IntField()


    def to_json(self):
        return {
            
            "course":str(self.course.id) if self.course else None,
            "year":str(self.year.id) if self.year else None,
            "subject":str(self.subject.id) if self.subject else None,
            "user":str(self.user.id) if self.user else None,
            "completed":self.completed,
            "total_time_taken_pages":self.total_time_taken_pages,
            "total_time_taken_layer":self.total_time_taken_layer,
            "total_page_count":self.total_page_count,
            "completed_page_count":self.completed_page_count,
            "total_layer_count":self.total_layer_count,
            "completed_layer_count":self.completed_layer_count
            }

    
    def with_key(self):
        return {
            "coures":self.course.to_json() if self.course else None,
            "year":self.year.to_json() if self.year else None,
            "subject":self.subject.to_json() if self.subject else None,
            "user":str(self.user.id)if self.user else None,
            "completed":self.completed,
            "total_time_taken_pages":self.total_time_taken_pages,
            "total_time_taken_layer":self.total_time_taken_layer,
            "total_page_count":self.total_page_count,
            "completed_page_count":self.completed_page_count,
            "total_layer_count":self.total_layer_count,
            "completed_layer_count":self.completed_layer_count
            
        }