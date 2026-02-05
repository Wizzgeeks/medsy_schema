from mongoengine import ( Document, StringField, ReferenceField, DateTimeField,EmbeddedDocument,IntField,EmbeddedDocumentField,ListField,CASCADE)
from datetime import datetime,timezone
from Models.assessment import Assessment


class PenaltyRule(EmbeddedDocument):
    switch_no = IntField(required=True)
    action = StringField(required=True,choices=("warning", "penalty", "lock", "submit"))
    seconds = IntField(default=0)

    def to_json(self):
        return {
            "switch_no": self.switch_no,
            "action": self.action,
            "seconds": self.seconds,
        }


class AssessmentSecurityPolicy(Document):
    assessment = ReferenceField(Assessment,reverse_delete_rule=CASCADE,required=True,unique=True)
    tabs_switch_penalty = ListField(EmbeddedDocumentField(PenaltyRule),default=list)
    max_tab_switch_allowed = IntField(default=0)
    minimize_penalty = ListField(EmbeddedDocumentField(PenaltyRule),default=list)
    max_minimize_allowed = IntField(default=0)
    created_at = DateTimeField(default=lambda: datetime.now(timezone.utc))
    updated_at = DateTimeField(null=True)


    def to_json(self):
        return {
            "id": str(self.id),
            "assessment_id": str(self.assessment.id) if self.assessment else None,
            "tabs_switch_penalty": [
                rule.to_json() for rule in self.tabs_switch_penalty
            ],
            "max_tab_switch_allowed": self.max_tab_switch_allowed,
            "minimize_penalty": [
                rule.to_json() for rule in self.minimize_penalty
            ],
            "max_minimize_allowed": self.max_minimize_allowed,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }
