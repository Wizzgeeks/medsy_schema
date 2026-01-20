from mongoengine import Document,StringField,ReferenceField,DateTimeField,IntField,BooleanField,CASCADE
from Models.course_model import Course
from Models.actions import Action
from datetime import datetime,timezone

class Action_coins(Document):
    course = ReferenceField(Course,reverse_delete_rule=CASCADE,required=True)
    name = StringField()
    coins = IntField(default=0)
    created_at = DateTimeField(default=datetime.now(timezone.utc))
    active = BooleanField(default=True)
    action = ReferenceField(Action,reverse_delete_rule=CASCADE,required=True)

    def to_json(self):
        return {
            "id": str(self.id),
            "course":str(self.course.id) if self.course else None,
            "name":self.name,
            "coins":self.coins if self.coins else 0,
            "active":self.active if self.active else False,
            "action":self.action.to_json() if self.action else None,
            "created_at": self.created_at.strftime('%d/%m/%Y'),
        }
    