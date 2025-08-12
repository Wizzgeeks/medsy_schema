from mongoengine import Document, ReferenceField, StringField,ListField,CASCADE
from Models.user_model import User
from datetime import datetime,timezone

class Active_study_time(Document):
    user = ReferenceField(User, required=True, reverse_delete_rule=CASCADE)
    date = StringField(default=lambda: datetime.now(timezone.utc).strftime('%d-%m-%Y'))
    study_time = ListField(required=True)

    def to_json(self):
        return {
            "id": str(self.id),
            "user": str(self.user.id) if self.user else None,
            "date": self.date,
            "study_time": self.study_time,
        }
