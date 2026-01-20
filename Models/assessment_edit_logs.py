from mongoengine import ( Document, StringField, ReferenceField, DateTimeField, CASCADE,NULLIFY,DictField)
from datetime import datetime,timezone
from Models.admin_model import Admin
from Models.assessment import Assessment

class AssessmentEditLogs(Document):
    updated_by = ReferenceField(Admin,reverse_delete_rule=NULLIFY,required=True)
    assessment_id = ReferenceField(Assessment, reverse_delete_rule=CASCADE,required=True)
    method = StringField()
    table_name = StringField()
    updated_data = DictField()
    existing_data = DictField()
    remarks = StringField(required=True)
    created_at = DateTimeField(default=lambda: datetime.now(timezone.utc))
    

    def to_json(self):
        return {
            "id": str(self.id),
            "assessment_id": str(self.assessment_id.id) if self.assessment_id else None,
            "method": self.method,
            "table_name": self.table_name,
            # "updated_data": self.updated_data,
            # "existing_data": self.existing_data,
            "updated_by": {"id": str(self.updated_by.id),"name": self.updated_by.name,"admin_id": self.updated_by.admin_id} if self.updated_by else {},
            "remarks": self.remarks,
            "created_at": self.created_at.strftime("%I:%M %p %b %d, %Y").lower() if self.created_at else None,
        }
        
    