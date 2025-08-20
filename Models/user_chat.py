from Models.layer3_page_model import Layer3_page
from Models.layer2_page_model import Layer2_page
from Models.layer1_page_model import Layer1_page
from Models.layer_1_model import Layer_1
from Models.layer_2_model import Layer_2
from Models.layer_3_model import Layer_3
from Models.subject_page_model import Subject_page
from Models.user_model import User
from Models.subject_model import Subject
from mongoengine import Document,ReferenceField,StringField,IntField,ListField,DictField,CASCADE

class User_Chat(Document):
    user=ReferenceField(User,reverse_delete_rule=CASCADE,required=True)
    subject=ReferenceField(Subject,reverse_delete_rule=CASCADE)
    layer1 = ReferenceField(Layer_1,reverse_delete_rule=CASCADE)
    layer2 = ReferenceField(Layer_2,reverse_delete_rule=CASCADE)
    layer3 = ReferenceField(Layer_3,reverse_delete_rule=CASCADE)
    layer1_page=ReferenceField(Layer1_page,reverse_delete_rule=CASCADE)
    layer2_page=ReferenceField(Layer2_page,reverse_delete_rule=CASCADE)
    layer3_page=ReferenceField(Layer3_page,reverse_delete_rule=CASCADE)
    subject_page=ReferenceField(Subject_page,reverse_delete_rule=CASCADE)
    chat=ListField(DictField())

    def to_json(self):
        return{
            "user":str(self.user.id) if self.user else None,
            "layer1_page":str(self.layer1_page.id ) if self.layer1_page else None,
            "layer2_page":str(self.layer2_page.id) if self.layer2_page else None,
            "layer3_page":str(self.layer2_page.id) if self.layer2_page else None,
            "chat":self.chat
        }
