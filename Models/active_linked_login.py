from mongoengine import Document,ReferenceField,DictField,ListField
from Models.user_model import User


class Linked_logins(Document):
    user=ReferenceField(User,required=True,unique=True,reverse_delete_rule=2)
    Linked_login=ListField(DictField())

    def to_json(self):
        return {
            "user":self.user.to_json(),
            "Linked_login":self.Linked_login if self.Linked_login else None
        }