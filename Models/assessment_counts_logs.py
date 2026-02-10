from mongoengine import ( Document, StringField, ReferenceField, DateTimeField, CASCADE,DictField)
from datetime import datetime,timezone
from Models.user_model import User

class AssessmentCountsLogs(Document):
    user = ReferenceField(User,reverse_delete_rule=CASCADE,required=True)
    logs_data = DictField()
    assessment_counts = DictField()
    created_at = DateTimeField(default=lambda: datetime.now(timezone.utc))
    

    def to_json(self):
        return {
            "id": str(self.id),
            "user": {"id": str(self.user.id),"name": self.user.username} if self.user else {},
            "logs_data": self.logs_data,
            "assessment_counts": self.assessment_counts,
            "created_at": self.created_at.strftime("%I:%M %p %b %d, %Y").lower() if self.created_at else None,
        }
        
    