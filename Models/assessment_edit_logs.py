from mongoengine import ( Document, StringField, ReferenceField, DateTimeField, CASCADE)
from datetime import datetime,timezone
from Models.admin_model import Admin
from Models.assessment import Assessment

class AssessmentEditLogs(Document):
    assessment_id = ReferenceField(Assessment, reversedelete_rule=CASCADE)
    updated_by = ReferenceField(Admin, required=True, reversedelete_rule=CASCADE)
    remarks = StringField(required=True)
    created_at = DateTimeField(default=lambda: datetime.now(timezone.utc))
    

    def to_json(self):
        return {
            "id": str(self.id),
            "assessment_id": str(self.assessment_id.id) if self.assessment_id else None,
            "updated_by": {"id": str(self.updated_by.id),"name": self.updated_by.name,"admin_id": self.updated_by.admin_id} if self.updated_by else {},
            "remarks": self.remarks,
            "created_at": self.created_at.isoformat() if self.created_at else None,
        }
        
    