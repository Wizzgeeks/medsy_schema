from mongoengine import Document,StringField,IntField,ReferenceField,DateTimeField,ListField,DictField
from Models.admin_model import Admin
from Models.course_model import Course
from datetime import datetime
from Models.layer1_page_model import Layer1_page
from Models.layer2_page_model import Layer2_page
from Models.layer3_page_model import Layer3_page

class Job_detail(Document):
    course = ReferenceField(Course,reverse_delete_rule=2,required=True)
    created_by=ReferenceField(Admin,required=True,reverse_delete_rule=2)
    created_at = DateTimeField(default=datetime.utcnow)
    target=StringField(choices=['Layer1_page_creation_job','Layer2_page_creation_job','Layer3_page_creation_job'],required=True)
    detail=StringField()
    completed_count=IntField()
    total_count=IntField()
    status=StringField()
    layer1_page = ReferenceField(Layer1_page, reverse_delete_rule=2)
    layer2_page = ReferenceField(Layer2_page, reverse_delete_rule=2)
    layer3_page = ReferenceField(Layer3_page, reverse_delete_rule=2)

    def to_json(self):
        return{
            "course":str(self.course.id) if self.course else None,
            "created_by":str(self.created_by.id) if self.created_by else None,
            "created_at":str(self.created_at),
            "target":self.target,
            "detail":self.detail,
            "completed_count":self.completed_count,
            "total_count":self.total_count,
            "status":self.status,
            "layer1_page": str(self.layer1_page.id) if self.layer1_page else None,
            "layer2_page": str(self.layer2_page.id) if self.layer2_page else None,
            "layer3_page": str(self.layer3_page.id) if self.layer3_page else None,

        }