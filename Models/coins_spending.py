from mongoengine import Document,StringField,ReferenceField,DateTimeField,IntField,CASCADE
from Models.user_model import User
from datetime import datetime,timezone

class Coins_spending(Document):
    user = ReferenceField(User,reverse_delete_rule=CASCADE,required=True)
    used_for = StringField()
    coins = IntField()
    date = DateTimeField(default=datetime.now(timezone.utc))

    def to_json(self):
        return {
            "id": str(self.id),
            "user":str(self.user.id) if self.user else None,
            "used_for":self.used_for,
            "coins":self.coins if self.coins else 0,
            "date": self.date.strftime('%d/%m/%Y'),
        }
    