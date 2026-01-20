from mongoengine import Document, ReferenceField,StringField,CASCADE
from Models.user_model import User
from datetime import datetime,timezone

class Active_user_details(Document):  
    user = ReferenceField(User, reverse_delete_rule=CASCADE,required=True)
    date = StringField(default=lambda: datetime.now(timezone.utc).strftime('%d-%m-%Y'))

    def to_json(self):
        return {
            "id": str(self.id),
            "user": str(self.user.id) if self.user else None,
            "date": self.date if self.date else None
        }
