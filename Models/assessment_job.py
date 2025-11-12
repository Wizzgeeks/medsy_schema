from mongoengine import Document,StringField,ReferenceField,DateTimeField,ListField,DictField,CASCADE,BooleanField
from Models.admin_model import Admin
from Models.course_model import Course
from datetime import datetime,timezone
from Models.assessment import Assessment

class AssessmentJob(Document):
    course = ReferenceField(Course,reverse_delete_rule=CASCADE,required=True)
    assessment = ReferenceField(Assessment,reverse_delete_rule=CASCADE,required=False)
    created_by=ReferenceField(Admin,required=True,reverse_delete_rule=CASCADE)
    created_at = DateTimeField(default=datetime.now(timezone.utc))
    detail=StringField()
    completed=BooleanField(default=False)
    status=StringField()
    logs=ListField(DictField()) 
    conversation = ListField(default=[])
    job_type=StringField(choices=["question_generation","tags_generation",""])
    updated_at = DateTimeField(null=True)


    def to_json(self):
        return{
            'id':str(self.id),
            "course":self.course.name if self.course else None,
            "assessment":str(self.assessment.id) if self.assessment else None,
            "created_by":self.created_by.name if self.created_by else None,
            'updated_at':str(self.updated_at) if self.updated_at else None,
            "created_at":str(self.created_at),
            "detail":self.detail,
            "status":self.status,
            "logs":self.logs,
            "completed":self.completed,
            "conversation":self.conversation,
            "job_type":self.job_type,

        }