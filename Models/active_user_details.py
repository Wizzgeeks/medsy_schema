from mongoengine import Document, ReferenceField,StringField
from Models.user_model import User
from datetime import datetime,timezone

class Active_user_details(Document):  
    user = ReferenceField(User, required=True, reverse_delete_rule=2)
    date = StringField(default=lambda: datetime.now().strftime('%d-%m-%Y'))

    def to_json(self):
        return {
            "id": str(self.id),
            "user": str(self.user.id) if self.user else None,
            "date": self.date if self.date else None
        }
