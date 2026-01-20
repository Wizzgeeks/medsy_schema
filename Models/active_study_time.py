from mongoengine import Document, ReferenceField, StringField,ListField,CASCADE,IntField,DateTimeField
from Models.user_model import User
from datetime import datetime,timezone

class Active_study_time(Document):
    user = ReferenceField(User, reverse_delete_rule=CASCADE,required=True)
    date = StringField(default=lambda: datetime.now(timezone.utc).strftime('%d-%m-%Y'))
    study_time = ListField(required=True)
    total_time_spent = IntField(default=0)
    last_ping_at = DateTimeField()

    def to_json(self):
        return {
            "id": str(self.id),
            "user": str(self.user.id) if self.user else None,
            "date": self.date,
            "study_time": self.study_time,
            "total_time_spent": self.total_time_spent if self.total_time_spent else 0
        }
