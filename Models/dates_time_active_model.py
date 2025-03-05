from mongoengine import Document,ReferenceField,DateTimeField
from Models.user_model import User
from datetime import datetime


class Active(Document):  
    user = ReferenceField(User,required=True,reverse_delete_rule=2)
    out_time = DateTimeField(default=datetime.utcnow)
    date = DateTimeField(default=datetime.utcnow)



    def to_json(self):
        return {
            "id":str(self.id),
            "user":str(self.user.id) if self.user else None,
            "date": str(self.date),
            "out_time": str(self.out_time),
        }