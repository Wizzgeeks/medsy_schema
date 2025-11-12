from mongoengine import ( Document, ReferenceField, DateTimeField, IntField, BooleanField ,CASCADE,ListField,DictField)
from datetime import datetime,timezone
from Models.assessment import Assessment
from Models.user_model import User


class AssessmentResult(Document):
    user = ReferenceField(User, reverse_delete_rule=CASCADE, required=True)
    assessment = ReferenceField(Assessment,reverse_delete_rule=CASCADE,required=True)
    completed_time = DateTimeField(null=True)
    result_data = ListField(DictField())
    marks = IntField()
    completed = BooleanField()
    created_at = DateTimeField(default=lambda: datetime.now(timezone.utc))
    updated_at = DateTimeField(null=True)
    

    def to_json(self):
        return {
            "id": str(self.id),
            "user": str(self.user.id) if self.user else None,
            "assessment": self.assessment.to_json() if self.assessment else None,
            "completed_time": self.completed_time.isoformat() if self.completed_time else None,
            "result_data": self.result_data,
            "marks": self.marks,
            "completed": self.completed,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }
