from mongoengine import Document,StringField,IntField,ReferenceField,DateTimeField,CASCADE
from Models.admin_model import Admin
from Models.course_model import Course
from datetime import datetime,timezone
from Models.prompt_model import Prompt
from Models.dependent_component import Dependent_components

class Prompt_ctc_job(Document):
    course = ReferenceField(Course,reverse_delete_rule=CASCADE,required=True)
    created_by=ReferenceField(Admin,reverse_delete_rule=CASCADE,required=True)
    created_at = DateTimeField(default=datetime.now(timezone.utc))
    target=StringField(choices=['Subject_prompt_ctc_apply_job','Layer1_prompt_ctc_apply_job','Layer2_prompt_ctc_apply_job','Layer3_prompt_ctc_apply_job'],required=True)
    detail=StringField()
    completed_count=IntField()
    total_count=IntField()
    status=StringField()
    ctc = ReferenceField(Dependent_components, reverse_delete_rule=CASCADE,required=True)
    prompt = ReferenceField(Prompt, reverse_delete_rule=CASCADE,required=True)
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
            "ctc":self.ctc if self.ctc else None,
            "prompt": str(self.prompt.id),


        }