from mongoengine import ( Document, ReferenceField, DateTimeField, IntField, BooleanField ,CASCADE,ListField,DictField,StringField)
from datetime import datetime,timezone
from Models.assessment import Assessment
from Models.user_model import User


class AssessmentResult(Document):
    attendance = BooleanField(default=True)
    user = ReferenceField(User, reverse_delete_rule=CASCADE, required=True)
    assessment = ReferenceField(Assessment,reverse_delete_rule=CASCADE,required=True)
    completed_time = DateTimeField(null=True)
    mcq_marks = IntField(default=0)
    descriptive_marks = IntField(default=0)
    mcq_attempted = IntField(default=0)
    descriptive_attempted = IntField(default=0)
    total_attempted = IntField(default=0)
    not_attempted = IntField(default=0)
    max_marks = IntField(default=0)
    percentage = IntField(default=0)
    result_data = ListField(DictField())
    marks = IntField(default=0)
    analytics_data = DictField()
    completed = BooleanField(default=False)
    eval_status = StringField(default="Incomplete",choices=["Incomplete","Completed","Pending","InProgress"])
    created_at = DateTimeField(default=lambda: datetime.now(timezone.utc))
    updated_at = DateTimeField(null=True)
    

    def to_json(self):
        return {
            "id": str(self.id),
            "user": str(self.user.id) if self.user else None,
            "assessment": str(self.assessment.id) if self.assessment else None,
            "completed_time": self.completed_time.isoformat() if self.completed_time else None,
            "mcq_marks": self.mcq_marks,
            "descriptive_marks": self.descriptive_marks,
            "mcq_attempted": self.mcq_attempted,
            "descriptive_attempted": self.descriptive_attempted,
            "total_attempted": self.total_attempted,
            "not_attempted": self.not_attempted,
            "max_marks": self.max_marks,
            "percentage": self.percentage,
            "result_data": self.result_data,
            "marks": self.marks,
            "completed": self.completed,
            "analytics_data": self.analytics_data,
            "eval_status": self.eval_status,
            "attendance": self.attendance,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }
        
    def to_get(self):
        return {
            "id": str(self.id),
            "user": {"id":str(self.user.id),"name":self.user.username,"user_id":self.user.user_id} if self.user else {},
            "assessment": {"id":str(self.assessment.id),"name":self.assessment.name,"test_type":self.assessment.test_type,"category":self.assessment.category,"total_marks":self.assessment.total_marks,"month_year":self.assessment.month_year.isoformat(),"course":self.assessment.course.name,"year":self.assessment.year.year,"course_id":str(self.assessment.course.id),"year_id":str(self.assessment.year.id)} if self.assessment else {},
            "completed_time": self.completed_time.isoformat() if self.completed_time else None,
            "mcq_marks": self.mcq_marks,
            "descriptive_marks": self.descriptive_marks,
            "mcq_attempted": self.mcq_attempted,
            "descriptive_attempted": self.descriptive_attempted,
            "total_attempted": self.total_attempted,
            "not_attempted": self.not_attempted,
            "max_marks": self.max_marks,
            "percentage": self.percentage,
            "result_data": self.result_data,
            "marks": self.marks,
            "completed": self.completed,
            # "analytics_data": self.analytics_data,
            "eval_status": self.eval_status,
            "attendance": self.attendance,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }
