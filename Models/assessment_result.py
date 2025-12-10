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
    attented_questions = IntField(default=0)
    max_marks = IntField(default=0)
    percentage = IntField(default=0)
    result_data = ListField(DictField())
    marks = IntField(default=0)
    analytics_data = ListField(DictField())
    completed = BooleanField(default=False)
    eval_status = StringField(default="Incomplete",choices=["Incomplete","Complete","Pending","InProgress"])
    created_at = DateTimeField(default=lambda: datetime.now(timezone.utc))
    updated_at = DateTimeField(null=True)
    

    def to_json(self):
        return {
            "id": str(self.id),
            "user": str(self.user.id) if self.user else None,
            "assessment": self.assessment.to_json() if self.assessment else None,
            "completed_time": self.completed_time.isoformat() if self.completed_time else None,
            "mcq_marks": self.mcq_marks,
            "descriptive_marks": self.descriptive_marks,
            "attented_questions": self.attented_questions,
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
