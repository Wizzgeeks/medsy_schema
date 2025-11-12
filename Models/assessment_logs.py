from mongoengine import ( Document, ReferenceField, DateTimeField, IntField, CASCADE,ListField,DictField)
from datetime import datetime,timezone
from Models.assessment import Assessment
from Models.user_model import User


class AssessmentLogs(Document):
    user = ReferenceField(User, reverse_delete_rule=CASCADE, required=True)
    assessment = ReferenceField(Assessment,reverse_delete_rule=CASCADE,required=True)
    tab_switch_times = IntField(default=0)
    logs = ListField(DictField())
    updated_at = DateTimeField(null=True)
    created_at = DateTimeField(default=lambda: datetime.now(timezone.utc))
    

    def to_json(self):
        return {
            "id": str(self.id),
            "user": str(self.user.id) if self.user else None,
            "assessment": self.assessment.to_json() if self.assessment else None,
            "tab_switch_times": self.tab_switch_times,
            "logs": self.logs,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
            "created_at": self.created_at.isoformat() if self.created_at else None,
        }
