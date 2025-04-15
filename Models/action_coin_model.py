from mongoengine import Document,StringField,ReferenceField,DateTimeField,IntField
from Models.course_model import Course
from datetime import datetime,timezone

class Action_coins(Document):
    course = ReferenceField(Course,required=True,reverse_delete_rule=2)
    name = StringField()
    coins = IntField(default=0)
    created_at = DateTimeField(default=datetime.now(timezone.utc))
    action = StringField()

    def to_json(self):
        return {
            "id": str(self.id),
            "course":str(self.course.id) if self.course else None,
            "name":self.name,
            "coins":self.coins if self.coins else None,
            "action":self.action if self.action else None,
            "created_at": self.created_at.strftime("%d %B %Y"),
        }
    