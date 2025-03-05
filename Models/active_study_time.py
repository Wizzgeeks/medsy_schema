from mongoengine import Document,ReferenceField,DateTimeField
from Models.user_model import User
from datetime import datetime


class Active_study_time(Document):
    user = ReferenceField(User,required=True,reverse_delete_rule=2)
    date = DateTimeField(unique=True,default=datetime.strftime('%Y-%m-%d'))
    in_time = DateTimeField(default=datetime.strftime('%H:%M %p'))
    out_time = DateTimeField(default=datetime.strftime('%H:%M %p'))


    def to_json(self):
        return {
            "id":str(self.id),
            "user":str(self.user.id) if self.user else None,
            "date": self.date,
            "in_time":self.in_time,
            "out_time":self.out_time
        }