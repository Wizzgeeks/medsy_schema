from mongoengine import Document,ReferenceField,IntField,CASCADE
from Models.user_model import User
from Models.layer_3_model import Layer_3
from Models.component_model import Component


class Layer3_component_time_spent(Document):
    layer3 = ReferenceField(Layer_3,reverse_delete_rule=CASCADE,required=True)
    user = ReferenceField(User,reverse_delete_rule=CASCADE,required=True)
    component = ReferenceField(Component,reverse_delete_rule=CASCADE,required=True)
    time_spent=IntField(required=True)


    def to_json(self):
        return {
            "layer3":str(self.layer3.id) if self.layer3 else None,
            "component":str(self.component.id) if self.component else None,
            "user":str(self.user.id) if self.user else None,
            "time_spent":self.time_spent
        }