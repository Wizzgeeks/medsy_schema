from mongoengine import Document, ReferenceField, StringField,CASCADE
from Models.user_model import User
from datetime import datetime,timezone

class Report(Document):
    user = ReferenceField(User, reverse_delete_rule=CASCADE,required=True)
    created_at = StringField(default=lambda: datetime.now(timezone.utc).strftime('%d-%m-%Y'))
    problem = StringField(required=True)
    category = StringField(required=True)
    location = StringField()

    def to_json(self):
        return {
            "id": str(self.id),
            "user": str(self.user.id) if self.user else None,
            "created_at": self.created_at,
            "location": self.location if self.location else None,
            "category": self.category,
            "problem": self.problem,
        }
