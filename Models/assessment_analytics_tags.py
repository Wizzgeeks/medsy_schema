from mongoengine import ( Document, ReferenceField, DateTimeField, BooleanField ,CASCADE,ListField,StringField)
from datetime import datetime,timezone
from Models.assessment import Assessment
from Models.institution_model import Institution
from Models.admin_model import Admin



class AssessmentConfigurations(Document):
    institution = ReferenceField(Institution,reverse_delete_rule=CASCADE,required=True)
    created_by = ReferenceField(Admin,reverse_delete_rule=CASCADE,required=True)
    assessment = ReferenceField(Assessment,reverse_delete_rule=CASCADE)
    is_active = BooleanField(default=True)
    cognitive_levels = ListField(StringField())
    created_at = DateTimeField(default=lambda: datetime.now(timezone.utc))
    updated_at = DateTimeField(null=True)
    

    def to_json(self):
        return {
            "id": str(self.id),
            "institution": str(self.institution.id) if self.institution else None,
            "created_by": str(self.created_by.id) if self.created_by else None,
            "is_active": self.is_active,
            "assessment": str(self.assessment.id) if self.assessment else None,
            "cognitive_levels": self.cognitive_levels if self.cognitive_levels else [],
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }
        
