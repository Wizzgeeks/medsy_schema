from mongoengine import Document, ReferenceField, StringField,ListField
from Models.user_model import User
from datetime import datetime

class Active_study_time(Document):
    user = ReferenceField(User, required=True, reverse_delete_rule=2)
    date = StringField(unique=True,default=lambda: datetime.now().strftime('%d-%m-%Y'))
    in_time = ListField(StringField(default=lambda: datetime.now().strftime('%I:%M %p')))
    out_time = ListField(StringField(default=lambda: datetime.now().strftime('%I:%M %p')))

    def to_json(self):
        return {
            "id": str(self.id),
            "user": str(self.user.id) if self.user else None,
            "date": self.date,
            "in_time": self.in_time,
            "out_time": self.out_time
        }
