from mongoengine import Document,ReferenceField,IntField,StringField,CASCADE
from Models.course_model import Course
from Models.user_model import User
from datetime import datetime,timezone

class Coin_management(Document):
    course = ReferenceField(Course,reverse_delete_rule=CASCADE,required=True)
    user = ReferenceField(User,reverse_delete_rule=CASCADE,required=True)
    coins = IntField(required=True)
    action = StringField(required=True)
    date = StringField(default=lambda: datetime.now(timezone.utc).strftime('%d-%m-%Y')) 


    def to_json(self):
        return {
            "id":str(self.id),
            "course":str(self.course.id) if self.course else None,
            "user":str(self.user.id) if self.user else None,
            "coins":self.coins,
            "action":self.action,
            "date":self.date
        }
    def with_key(self):
        return {
            "id":str(self.id),
            "course":self.course.to_json() if self.course else None,
            "user":self.user.to_json() if self.user else None,
            "coins":self.coins,
            "action":self.action,
            "date":self.date
        }