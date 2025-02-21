from mongoengine import Document,StringField,ReferenceField
from Models.course_model import Course


class Layer_3_details(Document):
    course = ReferenceField(Course,required=True,reverse_delete_rule=2)
    layer3_name = StringField(required=True,default='Layer 3')

    def to_json(self):
        return {
            'layer3_name': self.layer3_name
        }
            