from mongoengine import Document,StringField,ReferenceField
from Models.course_model import Course


class Layer_2_details(Document):
    course = ReferenceField(Course,required=True,reverse_delete_rule=2)
    layer2_name = StringField(required=True,default='Layer 2')

    def to_json(self):
        return {
            'layer2_name': self.layer2_name
        }
            