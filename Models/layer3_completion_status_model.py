from mongoengine import Document,ReferenceField,BooleanField
from Models.user_model import User
from Models.layer_3_model import Layer_3
from Models.component_model import Component


class Layer3_completion_status(Document):
    layer3 = ReferenceField(Layer_3,required=True,reverse_delete_rule=2)
    user = ReferenceField(User,required=True,reverse_delete_rule=2)
    component = ReferenceField(Component,required=True,reverse_delete_rule=2)
    completed=BooleanField(default=False)


    def to_json(self):
        return {
            "layer3":str(self.layer3.id) if self.layer3 else None,
            "component":str(self.component.id) if self.component else None,
            "user":str(self.user.id) if self.user else None,
            "completed":self.completed
        }