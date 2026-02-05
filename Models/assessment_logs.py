from mongoengine import ( Document, ReferenceField, DateTimeField, IntField, CASCADE,ListField,DictField,StringField)
from datetime import datetime,timezone
from Models.assessment import Assessment
from Models.user_model import User


class AssessmentLogs(Document):
    user = ReferenceField(User, reverse_delete_rule=CASCADE, required=True)
    assessment = ReferenceField(Assessment,reverse_delete_rule=CASCADE,required=True)
    tab_switch_times = IntField(default=0)
    minimized_times = IntField(default=0)
    user_start_time = DateTimeField(null=True)
    user_submit_time = DateTimeField(null=True)
    switch_logs = ListField(DictField())
    minimize_logs = ListField(DictField())
    assessment_logs = ListField(DictField())
    integrity_logs = ListField(DictField())
    logs = ListField(DictField())
    accesss_token = StringField()
    updated_at = DateTimeField(null=True)
    created_at = DateTimeField(default=lambda: datetime.now(timezone.utc))
    

    def to_json(self):
        return {
            "id": str(self.id),
            "user": str(self.user.id) if self.user else None,
            "assessment": self.assessment.to_json() if self.assessment else None,
            "tab_switch_times": self.tab_switch_times,
            "minimized_times": self.minimized_times,
            "user_start_time": self.user_start_time.isoformat() if self.user_start_time else None,
            "user_submit_time": self.user_submit_time.isoformat() if self.user_submit_time else None,
            "switch_logs": self.switch_logs,
            "minimize_logs": self.minimize_logs,
            "assessment_logs": self.assessment_logs,
            "integrity_logs": self.integrity_logs,
            "logs": self.logs,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
            "created_at": self.created_at.isoformat() if self.created_at else None,
        }
