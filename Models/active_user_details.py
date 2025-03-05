from mongoengine import Document,ReferenceField,DateTimeField
from Models.user_model import User
from datetime import datetime


class Active_user_details(Document):  
    user = ReferenceField(User,required=True,reverse_delete_rule=2)
    date = DateTimeField(unique=True,default=datetime.strftime('%Y-%m-%d'))

    def to_json(self):
        return {
            "id":str(self.id),
            "user":str(self.user.id) if self.user else None,
            "date": self.date
        }