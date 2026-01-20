from mongoengine import Document,StringField,IntField,ReferenceField,DateTimeField,ListField,DictField,CASCADE,BooleanField
from Models.admin_model import Admin
from Models.course_model import Course
from Models.institution_model import Institution
# from Models.year_model import Year
from datetime import datetime,timezone


class CourseCloneJob(Document):
    course = ReferenceField(Course,reverse_delete_rule=CASCADE,required=True)
    # year = ReferenceField(Year,reverse_delete_rule=CASCADE)
    institution = ReferenceField(Institution,reverse_delete_rule=CASCADE,required=True)
    created_by=ReferenceField(Admin,reverse_delete_rule=CASCADE,required=True)
    error_logs = ListField(DictField())
    completed_count=IntField()
    total_count=IntField()
    status = StringField(choices=['pending','in_progress','completed','failed','started'],default='started')
    completed=BooleanField(default=False)
    created_at = DateTimeField(default=datetime.now(timezone.utc))
    updated_at = DateTimeField(null=True)
    
    def to_json(self):
        return{
            'id':str(self.id),
            "course":self.course.name if self.course else None,
            # "year":self.year.name if self.year else None,
            "institution":self.institution.name if self.institution else None,
            "created_by":self.created_by.name if self.created_by else None,
            'updated_at':str(self.updated_at) if self.updated_at else None,
            "created_at":str(self.created_at),
            "error_logs":self.error_logs,
            "completed_count":self.completed_count,
            "total_count":self.total_count,
            "status":self.status,
            "completed":self.completed

        }