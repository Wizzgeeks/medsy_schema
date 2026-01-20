from mongoengine import Document,StringField,IntField,ReferenceField,DateTimeField,ListField,DictField,CASCADE
from Models.admin_model import Admin
from Models.course_model import Course
from datetime import datetime,timezone
from Models.layer1_page_model import Layer1_page
from Models.layer2_page_model import Layer2_page
from Models.layer3_page_model import Layer3_page
from Models.prompt_content_model import Prompt_content
from Models.subject_page_model import Subject_page

class Prompt_job(Document):
    course = ReferenceField(Course,reverse_delete_rule=CASCADE,required=True)
    created_by=ReferenceField(Admin,reverse_delete_rule=CASCADE,required=True)
    created_at = DateTimeField(default=datetime.now(timezone.utc))
    target=StringField(choices=['Subject_prompt_apply_job','Layer1_prompt_apply_job','Layer2_prompt_apply_job','Layer3_prompt_apply_job'],required=True)
    detail=StringField()
    completed_count=IntField()
    total_count=IntField()
    status=StringField()
    layer1_page = ReferenceField(Layer1_page, reverse_delete_rule=CASCADE)
    layer2_page = ReferenceField(Layer2_page, reverse_delete_rule=CASCADE)
    layer3_page = ReferenceField(Layer3_page, reverse_delete_rule=CASCADE)
    subject_page = ReferenceField(Subject_page, reverse_delete_rule=CASCADE)
    component = StringField(choices=['image','video','conversation','content','mcq','test_series'])
    prompt = ReferenceField(Prompt_content, reverse_delete_rule=CASCADE,required=True)
    updated_at = DateTimeField(null=True)

    def to_json(self):
        return{
            "id":str(self.id),
            "course":self.course.to_json() if self.course else None,
            "created_by":self.created_by.to_json() if self.created_by else None,
            'updated_at':str(self.updated_at) if self.updated_at else None,
            "created_at":str(self.created_at),
            "target":self.target,
            "detail":self.detail,
            "completed_count":self.completed_count,
            "total_count":self.total_count,
            "status":self.status,
            "layer1_page": str(self.layer1_page.id) if self.layer1_page else None,
            "layer2_page": str(self.layer2_page.id) if self.layer2_page else None,
            "layer3_page": str(self.layer3_page.id) if self.layer3_page else None,
            "subject_page": str(self.subject_page.id) if self.subject_page else None,
            "component": self.component,
            "prompt": str(self.prompt.id),


        }