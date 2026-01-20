from mongoengine import ( Document, ReferenceField, DateTimeField, IntField, BooleanField ,CASCADE,NULLIFY,ListField,EmbeddedDocument,EmbeddedDocumentField,StringField)
from datetime import datetime,timezone
from Models.assessment import Assessment
from Models.institution_model import Institution
from Models.admin_model import Admin

class AttainmentLevel(EmbeddedDocument):
    level = IntField(required=True)
    min_score = IntField(required=True)
    max_score = IntField(required=True)
    description = StringField(default="")
    
    
    def to_json(self):
        return {
            "level": self.level if self.level else 0,
            "min_score": self.min_score if self.min_score else 0,
            "max_score": self.max_score if self.max_score else 0,
            "description": self.description,
        }


class AssessmentConfigurations(Document):
    institution = ReferenceField(Institution,reverse_delete_rule=CASCADE,required=True)
    created_by = ReferenceField(Admin,reverse_delete_rule=NULLIFY,required=True)
    assessment = ReferenceField(Assessment,reverse_delete_rule=CASCADE,required=True)
    is_active = BooleanField(default=True)
    hot_threshold = IntField()
    lot_threshold = IntField()
    attainment_level = ListField(EmbeddedDocumentField(AttainmentLevel))
    created_at = DateTimeField(default=lambda: datetime.now(timezone.utc))
    updated_at = DateTimeField(null=True)
    

    def to_json(self):
        return {
            "id": str(self.id),
            "institution": str(self.institution.id) if self.institution else None,
            "created_by": str(self.created_by.id) if self.created_by else None,
            "is_active": self.is_active,
            "hot_threshold": self.hot_threshold,
            "lot_threshold": self.lot_threshold,
            "attainment_level": [level.to_json() for level in self.attainment_level],
            "assessment": str(self.assessment.id) if self.assessment else None,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }
        
