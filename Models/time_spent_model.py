from mongoengine import Document,ReferenceField,StringField,ValidationError,ListField
from Models.layer_3_model import Layer_3
from Models.user_model import User

class Time_spent(Document):
    layer3 = StringField(required=True)
    user = ReferenceField(User,required=True,reverse_delete_rule=2)
    time_spent = StringField()

    def to_json(self):
        return {
            "id":str(self.id),
            "layer3":str(self.layer3.id) if self.layer3 else None,
            "user":str(self.user.id) if self.user else None,
            "time_spent":self.time_spent,
        }
    
    def with_key(self):
        return {
            "id":str(self.id),
            "layer3":self.layer3.to_json() if self.layer3 else None,
            "user":self.user.to_json() if self.user else None,
            "time_spent":self.time_spent,
        }
    
    def clean(self):
        if not self.time_spent:
            raise ValidationError("Time spent Cannot be empty")
        
    def update(self, **kwargs):
        self.clean()
        return super().update(**kwargs)
