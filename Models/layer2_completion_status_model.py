from mongoengine import Document,ReferenceField,BooleanField,CASCADE,IntField,ListField,DictField
from Models.user_model import User
from Models.layer_2_model import Layer_2
from Models.layer_1_model import Layer_1
from Models.year_model import Year
from Models.subject_model import Subject
from Models.course_model import Course
from Models.layer2_completion_status_model import get_default_mastery
class Layer2_completion_status(Document):
    course=ReferenceField(Course,required=True,reverse_delete_rule=CASCADE)
    year=ReferenceField(Year,required=True,reverse_delete_rule=CASCADE)
    subject=ReferenceField(Subject,required=True,reverse_delete_rule=CASCADE)
    layer1 = ReferenceField(Layer_1,reverse_delete_rule=CASCADE)
    layer2 = ReferenceField(Layer_2,required=True,reverse_delete_rule=2)
    user = ReferenceField(User,required=True,reverse_delete_rule=CASCADE)   
    completed=BooleanField(default=False)
    total_time_taken_pages=IntField()
    total_time_taken_layer3=IntField()
    total_page_count=IntField()
    completed_page_count=IntField()
    total_layer3_count=IntField()
    completed_layer3_count=IntField()
    mastery_l2 = ListField(DictField(), default=[get_default_mastery])
    l3_summary=ListField(DictField(),default=[lambda: get_l3_summary_mastery("l3")])


    def to_json(self):
        return {
            'course':str(self.course) if self.course else None,
            'year':str(self.year) if self.year else None,
            'subject':str(self.subject) if self.subject else None,
            'layer1':str(self.layer1) if self.layer1 else None,
            "layer2":str(self.layer2.id) if self.layer2 else None,
            "user":str(self.user.id) if self.user else None,
            "completed":self.completed,
            "total_time_taken_pages":self.total_time_taken_pages,
            "total_time_taken_layer3":self.total_time_taken_layer3,
            "total_page_count":self.total_page_count if self.total_page_count else 0,
            "completed_page_count":self.completed_page_count if self.completed_page_count else 0,
            "total_layer3_count":self.total_layer3_count if self.total_layer3_count else 0,
        }
    
    def with_key(self):
        return {
            'course':self.course.to_json() if self.course else None,
            'year':self.year.to_json() if self.year else None,
            'subject':self.subject.to_json() if self.subject else None,
            'layer1':self.layer1.to_json() if self.layer1 else None,
            "user":str(self.user.id) if self.user else None,
            "completed":self.completed,
            "total_time_taken_pages":self.total_time_taken_pages,
            "total_time_taken_layer3":self.total_time_taken_layer3,
            "total_page_count":self.total_page_count,
            "completed_page_count":self.completed_page_count,
            "total_layer3_count":self.total_layer3_count,
            
        }
def get_l3_summary_mastery(layer):
    return {
        f"direct_total_{layer}": 0,
        f"direct_completed_{layer}": 0,
        f"critical_total_{layer}": 0,
        f"critical_completed_{layer}": 0,
        f"reasoning_total_{layer}": 0,
        f"reasoning_completed_{layer}": 0,
        f"clinical_total_{layer}": 0,
        f"clinical_completed_{layer}": 0,
    }
    