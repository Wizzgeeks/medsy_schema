from mongoengine import Document,ReferenceField,IntField,CASCADE
from Models.user_model import User
from Models.layer_2_model import Layer_2
from Models.component_model import Component


class Layer2_component_time_spent(Document):
    layer2 = ReferenceField(Layer_2,reverse_delete_rule=CASCADE,required=True)
    user = ReferenceField(User,reverse_delete_rule=CASCADE,required=True)
    component = ReferenceField(Component,reverse_delete_rule=CASCADE,required=True)
    time_spent=IntField(required=True)



    def to_json(self):
        return {
            "layer2":str(self.layer2.id) if self.layer2 else None,
            "component":str(self.component.id) if self.component else None,
            "user":str(self.user.id) if self.user else None,
            "time_spent":self.time_spent
        }