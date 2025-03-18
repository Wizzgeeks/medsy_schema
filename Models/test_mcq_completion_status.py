from mongoengine import Document,ReferenceField,BooleanField,IntField
from Models.user_model import User
from Models.layer_1_model import Layer_1
from Models.layer_2_model import Layer_2
from Models.layer_3_model import Layer_3


class Test_completion_status(Document):
    user = ReferenceField(User,required=True,reverse_delete_rule=2)
    layer1 = ReferenceField(Layer_1,reverse_delete_rule=2)
    layer2 = ReferenceField(Layer_2,reverse_delete_rule=2)
    layer3 = ReferenceField(Layer_3,reverse_delete_rule=2)
    completed=BooleanField(default=False)
    total_marks=IntField()
    scored_marks=IntField()

    def to_json(self):
        return {
            "completed":self.completed if self.completed else False,
            "total_marks":self.total_marks,
            "scored_marks":self.scored_marks
        }
