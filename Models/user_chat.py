from Models.layer3_page_model import Layer3_page
from Models.layer2_page_model import Layer2_page
from Models.layer1_page_model import Layer1_page
from Models.user_model import User
from mongoengine import Document,ReferenceField,StringField,IntField,ListField,DictField

class User_Chat(Document):
    user=ReferenceField(User,reverse_delete_rule=2,required=True)
    layer1_page=ReferenceField(Layer1_page,reverse_delete_rule=2)
    layer2_page=ReferenceField(Layer2_page,reverse_delete_rule=2)
    layer3_page=ReferenceField(Layer3_page,reverse_delete_rule=2)
    chat=ListField(DictField)

    def to_json(self):
        return{
            "user":str(self.user.id) if self.user else None,
            "layer1_page":str(self.layer1_page.id ) if self.layer1_page else None,
            "layer2_page":str(self.layer2_page.id) if self.layer2_page else None,
            "layer3_page":str(self.layer2_page.id) if self.layer2_page else None,
            "chat":self.chat
        }
