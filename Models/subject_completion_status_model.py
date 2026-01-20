from mongoengine import Document,ReferenceField,BooleanField,CASCADE,IntField,ListField,DictField
from Models.user_model import User
from Models.course_model import Course
from Models.year_model import Year
from Models.subject_model import Subject
from Models.layer3_completion_status_model import get_default_mastery
from Models.layer2_completion_status_model import get_l3_summary_mastery

class Subject_completion_status(Document):
    course=ReferenceField(Course,reverse_delete_rule=CASCADE,required=True)
    year=ReferenceField(Year,reverse_delete_rule=CASCADE,required=True)
    subject=ReferenceField(Subject,reverse_delete_rule=CASCADE,required=True)
    user = ReferenceField(User,reverse_delete_rule=CASCADE,required=True)
    completed=BooleanField(default=False)
    total_time_taken_pages=IntField()
    total_time_taken_layer=IntField()
    total_page_count=IntField()
    completed_page_count=IntField()
    total_layer_count=IntField()
    completed_layer_count=IntField()
    mastery_subject = DictField(default=lambda: get_default_mastery())
    l1_summary=DictField(default=lambda: get_l3_summary_mastery("l1"))
    l2_summary=DictField(default=lambda:get_l3_summary_mastery("l2"))
    l3_summary=DictField(default=lambda:get_l3_summary_mastery("l3"))


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