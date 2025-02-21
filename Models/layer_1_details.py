from mongoengine import Document,StringField,ReferenceField
from Models.course_model import Course


class Layer_1_details(Document):
    course = ReferenceField(Course,required=True,reverse_delete_rule=2)
    layer1_name = StringField(required=True,default='Layer 1')

    def to_json(self):
        return {
            'layer1_name': self.layer1_name
        }
            